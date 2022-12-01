import sent2vec
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import nltk
import csv
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')
import sys


class data_transformer:

    def __init__(self):
        self.model_path = "./biosentvec_model/BioSentVec_PubMed_MIMICIII-bigram_d700.bin"
        self.model = sent2vec.Sent2vecModel()
        try:
            self.model.load_model(self.model_path)
        except Exception as e:
            print(e)
        print('model successfully loaded')

        csv.field_size_limit(sys.maxsize)
        print("init")  # never prints

    @staticmethod
    def preprocess_sentence(text):
        stop_words = set(stopwords.words('english'))
        text = text.replace('.', ' . ')
        text = text.replace('\'', ' \' ')
        text = text.lower()

        tokens = [token for token in word_tokenize(text) if token not in punctuation and token not in stop_words]

        return ' '.join(tokens)

    def convert_sentence_to_vector(self, sentence):
        sentence_vector = self.model.embed_sentence(self.preprocess_sentence(sentence))

        return sentence_vector

    @staticmethod
    def save_processed_data(fold_name, vector_dict, parent_folder, filename):

        # https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value

        with open("./data/" + parent_folder + "/" + fold_name + "/processed_" + filename + fold_name + ".csv",
                  "w") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in vector_dict.items():
                writer.writerow([key, value])

    def create_vector_dictionary(self, fold_dataframe):
        df_dict = fold_dataframe.to_dict("records")
        vector_dict = {}

        for row in df_dict:

            row_list = []

            for i in row:
                if str(row[i]) != "None":
                    if i != 0:
                        ith_vector = self.convert_sentence_to_vector(row[i])
                        row_list.append(ith_vector.tolist())

            vector_dict[row[0]] = row_list
        return vector_dict

    def process_fold_data(self, fold_name, filename):

        if fold_name:
            folder_path = "./data/unprocessed/" + fold_name + "/" + filename + ".csv"

            fold_dataframe = pd.read_csv(folder_path, header=None, sep='\n')
            fold_dataframe = fold_dataframe[0].str.split(',', expand=True)

            vector_dict = self.create_vector_dictionary(fold_dataframe)

            self.save_processed_data(fold_name, vector_dict, "processed", filename)

            # Most efficient way to loop through a dataframe is df.to_dict('records')
            # https://towardsdatascience.com/heres-the-most-efficient-way-to-iterate-through-your-pandas-dataframe-4dad88ac92ee#:~:text=Vectorization%20is%20always%20the%20first,up%20for%2020%20million%20records.
        else:
            exit

    def fetch_processed_data_fold(self, fold_name):
        filename = "TrainingSet"
        if fold_name:
            folder_path = "./data/processed/" + fold_name + "/processed_" + filename + fold_name + ".csv"
            with open(folder_path) as csv_file:
                reader = csv.reader(csv_file)
                diagnosis_symptoms_dict = dict(reader)
                sorted_symptoms_dict = {}
                for entries in diagnosis_symptoms_dict.keys():

                    full_string_values = diagnosis_symptoms_dict.get(entries).lstrip('[[[').rstrip(']]]')
                    full_string_values = full_string_values.split("]], [[")
                    sorted_values = []
                    for value_list in full_string_values:
                        vector_list = []
                        each_sentence = value_list.split(",")

                        for string_vector in each_sentence:
                            result = float(string_vector)
                            vector_list.append(result)

                        sorted_values.append(vector_list)

                    sorted_values = sorted(sorted_values)
                    sorted_symptoms_dict[entries] = sorted_values

                # {k: v for k, v in sorted(sorted_symptoms_dict.items(), key=lambda item: print(item))}
                sorted_values = sorted(sorted_symptoms_dict.values())  # Sort the values

                self.save_processed_data(fold_name, sorted_symptoms_dict, "sorted", filename)

    def fetch_sorted_data(self, fold_name):
        if fold_name:
            folder_path = "./data/sorted/" + fold_name + "/processed_TrainingSet" + fold_name + ".csv"

            with open(folder_path) as csv_file:
                reader = csv.reader(csv_file)
                diagnosis_symptoms_dict = dict(reader)
                sorted_symptoms_dict = self.read_file_to_sorted_dictionary(diagnosis_symptoms_dict)

                return sorted_symptoms_dict

            close()

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

    def rearrange(self, unordered_dict, fold_name):
        filename = "TrainingSet"
        order_dict = {}
        for key in unordered_dict.keys():
            order_dict[key] = unordered_dict[key][0]

        order_dict = {k: v for k, v in sorted(order_dict.items(), key=lambda item: item[1])}

        order_dict_to_save = {}
        for key in order_dict.keys():
            order_dict_to_save[key] = unordered_dict[key]

        self.save_processed_data(fold_name, order_dict_to_save, "ordered", filename)
