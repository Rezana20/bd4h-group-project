import csv
import itertools
import sys
import bisect
from fileinput import close

import numpy as np


class cds:

    def __init__(self):
        csv.field_size_limit(sys.maxsize)
        print("init")  # never prints

    def read_file_to_sorted_dictionary(self, diagnosis_symptoms_dict):
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

    # exact search
    def find_in_sorted_list(self, elem, sorted_list):
        # https://docs.python.org/3/library/bisect.html
        'Locate the leftmost value exactly equal to x'
        i = bisect.bisect_left(sorted_list, elem)
        if i != len(sorted_list) and sorted_list[i] == elem:
            return "exists"
        return -1

    def fetch_sorted_data(self, fold_name):
        if fold_name:
            folder_path = "./data/ordered/" + fold_name + "/processed_TrainingSet" + fold_name + ".csv"

            with open(folder_path) as csv_file:
                reader = csv.reader(csv_file)
                diagnosis_symptoms_dict = dict(reader)
                sorted_symptoms_dict = self.read_file_to_sorted_dictionary(diagnosis_symptoms_dict)

                return sorted_symptoms_dict

            close()

    # def cosine_similarity(self, target_element, existing_patient_element):
    #     list_argmax_cos = []
    #     print(existing_patient_element)
    #
    #     for x in range(len(target_element)-1):
    #         temp = [np.cos(target_element[x]), np.cos(existing_patient_element[x])]
    #         temp_argmax = np.argmax(temp, axis=0)
    #         list_argmax_cos.append(temp[temp_argmax])
    #
    #     sum_argmax = sum(list_argmax_cos)
    #
    #     result = sum_argmax / 700
    #
    #     print(result)
    #
    #     return result

    def cosine_similarity(self, target_element, existing_patient_element):
        list_argmax_cos = []

        for x in range(len(target_element[0]) - 1):
            temp = [np.cos(target_element[0][x]), np.cos(existing_patient_element[0][x])]
            temp_argmax = np.argmax(temp, axis=0)
            list_argmax_cos.append(temp[temp_argmax])

        sum_argmax = sum(list_argmax_cos)

        result = sum_argmax / 700
        return result

    def semantic_similarity(self, target_element, existing_patient_element):
        temp = 0
        m = len(target_element)
        n = len(existing_patient_element)
        for x in existing_patient_element:
            temp += max([(np.array(x) @ np.array(y)) / (np.linalg.norm(x) * np.linalg.norm(y)) if np.linalg.norm(
                x) * np.linalg.norm(y) != 0 else 0 for y in target_element])
        return temp / max(n, m)

    def similarity_search_n_folds(self, test_fold_dict, alpha, k, fold_dict, fold_index):
        top_k = []

        for target_patient_key in test_fold_dict:
            similarity_comparison_dictionary = {}
            for fold_key in range(k):
                # print("Comparing test target patient: ", target_patient_key, " to each diagnosis in fold ->: ",
                #       fold_index[fold_key])

                row_similarity_list = []
                for target_patient_symptom_vector in range(len(test_fold_dict[target_patient_key])):
                    target_patient_similarity_list = []
                    for fold_patient_symptom_vector in range(len((fold_dict[fold_index[fold_key]]))):
                        target_patient = test_fold_dict[target_patient_key][target_patient_symptom_vector]
                        historic_patient = fold_dict[fold_index[fold_key]][fold_patient_symptom_vector]

                        similarity = self.semantic_similarity(target_patient, historic_patient)
                        target_patient_similarity_list.append(similarity)
                        # similarity = self.cosine_similarity(target_patient, historic_patient)

                        # if similarity > alpha:
                        #     target_patient_similarity_list.append(similarity)

                    row_similarity_list.append(np.mean(target_patient_similarity_list))

                average_row_similarity = np.mean(row_similarity_list)

                similarity_comparison_dictionary[
                    target_patient_key + "," + fold_index[fold_key]] = average_row_similarity

            self.predictions(similarity_comparison_dictionary)

        #     Todo store the dictionary results in folder under Fold name

        # Order similarity_comparison_dictionary by value, and then select top k and return that.
        # similarity_comparison_dictionary = {combination_key: similarity_value for combination_key, similarity_value in
        #                                     sorted(similarity_comparison_dictionary.items(), key=lambda item: item[1], reverse=True)[:k]}

        # print(similarity_comparison_dictionary)

        # return similarity_comparison_dictionary

    def search_fold(self, fold_name):

        # Todo read test symptoms and search fold

        # fetches the ordered fold name
        print("compare fold to dummy test ->", fold_name)
        ordered_fold_dict = self.fetch_sorted_data(fold_name)

        # [0] = whole [[[][]]]
        # [0][0] = []
        # [0][0][0] is the first element of the first

        print("set alpha 0.7")
        alpha_list = [0.7]  # [0.7, 0.8, 0.9]
        print("set k to 5")
        max_k = 30


        # Todo read in the test folder
        print("read the test fold")
        test_dict = self.fetch_elem()

        print("create an index for searching the fold")
        ordered_fold_index = {k: i for k, i in enumerate(ordered_fold_dict.keys())}

        print("----------------")
        for alpha in alpha_list:
            print("alpha: ", alpha)
            self.similarity_search_n_folds(test_dict, alpha, max_k, ordered_fold_dict, ordered_fold_index)

    def fetch_elem(self):
        folder_path = "./data/ordered/Fold0/processed_TrainingSetFold0-test copy.csv"
        with open(folder_path) as csv_file:
            reader = csv.reader(csv_file)
            diagnosis_symptoms_dict = dict(reader)
            sorted_symptoms_dict = self.read_file_to_sorted_dictionary(diagnosis_symptoms_dict)
            close()
            return sorted_symptoms_dict

    def predictions(self, top_k_dictionary):
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
