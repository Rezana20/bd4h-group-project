import sent2vec
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import nltk
import csv

nltk.download('stopwords')
nltk.download('punkt')


class data_transformer:

    def __init__(self):
        self.model_path = "./biosentvec_model/BioSentVec_PubMed_MIMICIII-bigram_d700.bin"
        self.model = sent2vec.Sent2vecModel()
        try:
            self.model.load_model(self.model_path)
        except Exception as e:
            print(e)
        print('model successfully loaded')
        print("init")  # never prints

    def preprocess_sentence(self, text):
        stop_words = set(stopwords.words('english'))
        text = text.replace('.', ' . ')
        text = text.replace('\'', ' \' ')
        text = text.lower()

        tokens = [token for token in word_tokenize(text) if token not in punctuation and token not in stop_words]

        return ' '.join(tokens)

    def convert_sentence_to_vector(self, sentence):
        sentence_vector = self.model.embed_sentence(self.preprocess_sentence(sentence))

        return sentence_vector

    def save_processed_data(self, fold_name, vector_dict):

        # https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value

        with open("./data/processed/" + fold_name + "/processed_TrainingSet" + fold_name + ".csv", "w") as csv_file:
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

    def read_fold(self, fold_name):

        if fold_name:
            folder_path = "./data/unprocessed/" + fold_name + "/TrainingSet.csv"

            fold_dataframe = pd.read_csv(folder_path, header=None, sep='\n')
            fold_dataframe = fold_dataframe[0].str.split(',', expand=True)

            vector_dict = self.create_vector_dictionary(fold_dataframe)

            self.save_processed_data(fold_name, vector_dict)

            # Most efficient way to loop through a dataframe is df.to_dict('records')
            # https://towardsdatascience.com/heres-the-most-efficient-way-to-iterate-through-your-pandas-dataframe-4dad88ac92ee#:~:text=Vectorization%20is%20always%20the%20first,up%20for%2020%20million%20records.
        else:
            exit





