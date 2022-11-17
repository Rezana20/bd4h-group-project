import csv
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

    def disease_diagnosis(self, symptom_list):
        disease = "diabetes"

        # Todo import trained model
        model = "read trained model"

        # Todo read symptom_list pass it to trained model - determine the output and return the cds guess
        # disease = model.predict(symptom_list)

        return disease

    def cosine_similarity(self, target_element, existing_patient_element):
        list_argmax_cos = []

        for x in range(len(target_element)-1):
            temp = [np.cos(target_element[x]), np.cos(existing_patient_element[x])]
            temp_argmax = np.argmax(temp, axis=0)
            list_argmax_cos.append(temp[temp_argmax])

        sum_argmax = sum(list_argmax_cos)

        result = sum_argmax / 700

        print(result)

        return result

    def search_fold(self, fold_name, test_symptoms):

        # Todo read test symptoms and search fold
        # print(test_symptoms)

        ordered_dict = self.fetch_sorted_data(fold_name)

        # [0] = whole [[[][]]]
        # [0][0] = []
        # [0][0][0] is the first element of the first

        # create an index for searching
        index = {k: i for k, i in enumerate(ordered_dict.keys())}

        elem = self.fetch_elem()

        print(self.cosine_similarity(elem["103379_E coli septicemia"][1][0], elem["103379_E coli septicemia"][1][0]))

        list_yes_keys = []
        for keys in index.keys():
            ordered_dict[index[keys]][0]

            does_exist = self.find_in_sorted_list(elem["103379_E coli septicemia"][1][0], ordered_dict[index[keys]][0])

            if does_exist != -1:
                list_yes_keys.append(keys)

        print(list_yes_keys)

    def fetch_elem(self):
        folder_path = "./data/ordered/Fold0/processed_TrainingSetFold0-test.csv"
        with open(folder_path) as csv_file:
            reader = csv.reader(csv_file)
            diagnosis_symptoms_dict = dict(reader)
            sorted_symptoms_dict = self.read_file_to_sorted_dictionary(diagnosis_symptoms_dict)
            close()
            return sorted_symptoms_dict
