import csv
import itertools
import sys
import bisect
from fileinput import close
import time
import os.path
import re

import numpy as np


class cds:

    def __init__(self):
        csv.field_size_limit(sys.maxsize)
        print("init")  # never prints

    @staticmethod
    def read_file_to_sorted_dictionary(diagnosis_symptoms_dict):
        sorted_symptoms_dict = {}
        for entries in diagnosis_symptoms_dict.keys():

            full_string_values = diagnosis_symptoms_dict.get(entries).lstrip('[[[').rstrip(']]]')
            full_string_values = full_string_values.split("]], [[")
            sorted_values = []
            # This is the list of vectors per diag
            for symptom_vector_list in full_string_values:
                # This is the list of vectors broken into each vector
                symptom_vectors = symptom_vector_list.split("], [")
                total_symptom_vector_list = []
                # This is us converting each element in the vector to its float value and
                # adding it back to the a vector list

                for vector in symptom_vectors:
                    vector = vector.split(",")
                    single_symptom_vector_list = []
                    for string_vector in vector:
                        result = float(string_vector)
                        single_symptom_vector_list.append(result)
                    total_symptom_vector_list.append(single_symptom_vector_list)

                sorted_values.append(total_symptom_vector_list)

            sorted_values = sorted(sorted_values)
            sorted_symptoms_dict[entries] = sorted_values
        return sorted_symptoms_dict

    def fetch_input_data(self, filename):
        if filename:
            with open(filename) as csv_file:
                reader = csv.reader(csv_file)
                diagnosis_symptoms_dict = dict(reader)
                sorted_symptoms_dict = self.read_file_to_sorted_dictionary(diagnosis_symptoms_dict)

                return sorted_symptoms_dict

            close()

    @staticmethod
    def read_similarity_data(patient_similarity_dict):
        similarity_dict = {}
        for entry in patient_similarity_dict.keys():
            cleaned_patient_similarity_value = patient_similarity_dict[entry].lstrip('[(').rstrip(')]')
            patient_similarity_str = cleaned_patient_similarity_value.split("), (")
            top_k = {}
            for key_value_pair in patient_similarity_str:
                key_value_pair_split = key_value_pair.split(",")
                top_k[key_value_pair_split[0]] = float(key_value_pair_split[1])
            similarity_dict[entry] = top_k

        return similarity_dict

    def fetch_similarity_data(self, filename):
        if filename:
            with open(filename) as csv_file:
                reader = csv.reader(csv_file)
                patient_similarity_dict = dict(reader)
                similarity_dict = self.read_similarity_data(patient_similarity_dict)
                return similarity_dict

            close()

    # exact match search
    @staticmethod
    def find_in_sorted_list(elem, sorted_list):
        # https://docs.python.org/3/library/bisect.html
        'Locate the leftmost value exactly equal to x'
        i = bisect.bisect_left(sorted_list, elem)
        if i != len(sorted_list) and sorted_list[i] == elem:
            return "exists"
        return -1

    def calculate_top_k(self, foldname):
        print("We are attempting to calculate top k (30)")
        st = time.time()

        print("Fold 0....")
        self.create_and_store_top_30(foldname)

        # get the end time
        et = time.time()

        # get the execution time
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')

    @staticmethod
    def predictions(top_k_dictionary):
        folder_path = "./data/ordered/Fold0"
        precision = 0

        # P = (TP) / ( TP + TN)
        k_list = [1, 5, 10, 15, 20, 25, 30]
        ground_truth = ''
        precision_list_for_k = []
        for k in k_list:
            # print("result: ", dict(itertools.islice(top_k_dictionary.items(), k)))

            temp_k_dict = dict(itertools.islice(top_k_dictionary.items(), k))

            TP_count = 0
            precision_dict = {}

            for combination_key in temp_k_dict.keys():

                prediction_result = combination_key.split(",")
                ground_truth = prediction_result[0]
                prediction = prediction_result[1]

                if ground_truth == prediction:
                    TP_count += 1

            if TP_count != 0:
                P = TP_count / k
            else:
                P = 0

            precision_list_for_k.append(P)

            precision_dict[ground_truth] = precision_list_for_k

        with open(folder_path + "/precisionFold0.csv", "a") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in precision_dict.items():
                writer.writerow([key, value])

        pass

    @staticmethod
    def cosine_similarity(patient_vector_list, target_patient_vector_list):
        n = len(patient_vector_list)
        m = len(target_patient_vector_list)

        total_sum = 0
        for x in range(n):
            max_cos = 0
            for y in range(m):

                patient_vector = patient_vector_list[x]
                target_patient_vector = target_patient_vector_list[y]
                cos_x = 0
                cos_y = 0
                for element in range(700):
                    cos_x += np.cos(patient_vector[0][element]) / 700
                    cos_y += np.cos(target_patient_vector[0][element]) / 700

                x_vs_y_cos = [cos_x, cos_y]
                max_cos = x_vs_y_cos[np.argmax(x_vs_y_cos, axis=0)]
            total_sum += max_cos

        n_m_max = [n, m]

        return total_sum / n_m_max[np.argmax(n_m_max, axis=0)]

    def store_TP_TN(self, foldname, alpha):
        filename = "./data/processed/" + foldname + "/TopK_TestSet" + foldname + "_" + str(alpha) + ".csv"
        file_exists = self.do_something(filename)
        if file_exists:
            test_fold_alpha = self.fetch_similarity_data(filename)
            cumulative_TP = [0, 0, 0, 0, 0, 0, 0]
            cumulative_TN = [0, 0, 0, 0, 0, 0, 0]
            TP_dict = {}
            TP_TN_dict = {}

            for patient in test_fold_alpha.keys():
                # https://thispointer.com/remove-string-before-a-specific-character-in-python/
                ch = '_'
                pattern = ".*" + ch
                patient_diag = re.sub(pattern, '', patient)

                value_dict = test_fold_alpha[patient]
                value_index = {k: i for k, i in enumerate(value_dict.keys())}

                for k, v in value_index.items():
                    if re.sub(pattern, '', v.rstrip("'")) == patient_diag:
                        if patient not in TP_dict:
                            TP_dict[patient] = k

            for patient in test_fold_alpha.keys():
                if patient in TP_dict:
                    position = TP_dict[patient]
                    if position == 0:
                        for i in range(len(cumulative_TN)):
                            cumulative_TP[i] += 1
                    elif 1 <= position <= 4:
                        for i in range(1, 7):
                            cumulative_TP[i] += 1
                    elif 5 <= position <= 9:
                        for i in range(2, 7):
                            cumulative_TP[i] += 1
                    elif 10 <= position <= 14:
                        for i in range(3, 7):
                            cumulative_TP[i] += 1
                    elif 15 <= position <= 19:
                        for i in range(4, 7):
                            cumulative_TP[i] += 1
                    elif 20 <= position <= 24:
                        for i in range(5, 7):
                            cumulative_TP[i] += 1
                    elif 25 <= position <= 29:
                        for i in range(6, 7):
                            cumulative_TP[i] += 1
                else:
                    for i in range(len(cumulative_TN)):
                        cumulative_TN[i] += 1

            TP_TN_dict["TP"] = cumulative_TP
            TP_TN_dict["TN"] = cumulative_TN
            self.save_TP_TN_per_fold(TP_TN_dict, foldname, alpha)

    def similarity_search(self, test_data_dict, alpha, train_data_dictionary, train_fold_index, foldname):

        filename = "./data/processed/" + foldname + "/TopK_TestSet" + foldname + "_" + str(alpha) + ".csv"
        file_exists = self.do_something(filename)
        if not file_exists:
            test_fold_patient_dict = {}
            for patient in test_data_dict:
                # print("patient ", patient)
                similarity_dict = {}
                patient_vector_list = test_data_dict[patient]

                for target_patient in train_fold_index:
                    target_patient_vector_list = train_data_dictionary[train_fold_index[target_patient]]
                    max_precision = self.cosine_similarity(patient_vector_list, target_patient_vector_list)
                    if max_precision >= alpha:
                        similarity_dict[train_fold_index[target_patient]] = max_precision

                similarity_dict = sorted(similarity_dict.items(), key=lambda x: x[1], reverse=True)
                if len(similarity_dict) > 30:
                    test_fold_patient_dict[patient] = similarity_dict[:30]
                else:
                    test_fold_patient_dict[patient] = similarity_dict
                # break

            # print(test_fold_patient_dict)

            return test_fold_patient_dict
        else:
            pass

    def save_topk_data(self, foldname, vector_dict, alpha):
        # https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value
        filename = "./data/processed/" + foldname + "/TopK_TestSet" + foldname + "_" + str(alpha) + ".csv"

        file_exists = self.do_something(filename)

        if not file_exists:
            with open(filename, "w") as csv_file:
                writer = csv.writer(csv_file)
                for key, value in vector_dict.items():
                    writer.writerow([key, value])
        close()

    def save_TP_TN_per_fold(self, TP_TN_dict, foldname, alpha):
        filename = "./data/processed/" + foldname + "/TP_TN" + foldname + "_" + str(alpha) + ".csv"

        file_exists = self.do_something(filename)

        if not file_exists:
            with open(filename, "w") as csv_file:
                writer = csv.writer(csv_file)
                for key, value in TP_TN_dict.items():
                    writer.writerow([key, value])
        close()

    def do_something(self, filename):
        return os.path.exists(filename)

    def create_and_store_top_30(self, foldname):

        test_file_name = "./data/processed/" + foldname + "/processed_TestSet" + foldname + ".csv"
        train_file_name = "./data/processed/" + foldname + "/processed_TrainingSet" + foldname + ".csv"
        test_data_dict = self.fetch_input_data(test_file_name)
        train_data_dict = self.fetch_input_data(train_file_name)
        train_fold_index = {k: i for k, i in enumerate(train_data_dict.keys())}
        test_fold_index = {k: i for k, i in enumerate(test_data_dict.keys())}
        alpha = [0.70, 0.80, 0.90]

        for alp in alpha:
            test_fold_patient_dict = self.similarity_search(test_data_dict, alp, train_data_dict, train_fold_index,
                                                            foldname)
            self.save_topk_data(foldname, test_fold_patient_dict, alp)

        for alp in alpha:
            self.store_TP_TN(foldname, alp)
