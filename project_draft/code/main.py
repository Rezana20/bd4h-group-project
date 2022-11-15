# This is a sample Python script.
import csv
import data_transformer
import numpy as np


def patient_similarity():
    print("Module 3 CDS")


def diagnosis():
    print("Module 2 testing")


def data_sorting():
    print("Module 2, data pre-sorting")
    # data_trans = data_transformer.data_transformer()
    #
    # print("Fold0 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold0")
    #
    # print("Fold1 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold1")
    #
    # print("Fold2 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold2")
    #
    # print("Fold3 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold3")
    #
    # print("Fold4 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold4")
    #
    # print("Fold5 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold5")
    #
    # print("Fold6 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold6")
    #
    # print("Fold7 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold7")
    #
    # print("Fold8 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold8")
    #
    # print("Fold9 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold9")


def data_preprocessing():
    print("Module 1, data pre-processing")
    # data_trans = data_transformer.data_transformer()
    #
    # print("Fold0 pre-processing.....")
    # data_trans.read_fold("Fold0")
    # Gout NOS, Old myocardial infarct

    # print("Fold0 pre-processing.....")
    # data_trans.read_fold("Fold0")

    # print("Fold1 pre-processing.....")
    # data_trans.read_fold("Fold1")
    #
    # print("Fold2 pre-processing.....")
    # data_trans.read_fold("Fold2")
    #
    # print("Fold3 pre-processing.....")
    # data_trans.read_fold("Fold3")
    #
    # print("Fold4 pre-processing.....")
    # data_trans.read_fold("Fold4")
    #
    # print("Fold5 pre-processing.....")
    # data_trans.read_fold("Fold5")
    #
    # print("Fold6 pre-processing.....")
    # data_trans.read_fold("Fold6")
    #
    # print("Fold7 pre-processing.....")
    # data_trans.read_fold("Fold7")
    #
    # print("Fold8 pre-processing.....")
    # data_trans.read_fold("Fold8")
    #
    # print("Fold9 pre-processing.....")
    # data_trans.read_fold("Fold9")


if __name__ == '__main__':
    data_preprocessing()

    data_sorting()

    # diagnosis()

    patient_similarity()
    # creating list https://www.freecodecamp.org/news/the-python-sort-list-array-method-ascending-and-descending-explained-with-examples/
    # list1 = [-2.63524633e-02, -1.41732764e+00, -4.04191315e-01, 3.32329750e-01]
    # list2 = [1.32625699e-01, -4.62552309e-02, -1.02783442e+00, -1.50074446e+00]
    # list3 = [1.24941206e+00, 1.44566822e+00, 4.24575865e-01, 7.24694252e-01]
    #
    # test = np.array([list1, list2, list3])
    # print(sorted([list1, list2, list3]))

    # print("Create the sample symptoms diagnosis object")
    #
    # symptom_diagnosis_list = data_trans.create_symptoms_diagnosis_training_data()
    #
    # print("create corpus file from all input sentences")
    # data_trans.create_sent2vec_input_corpus(symptom_diagnosis_list)

    # print("Create admissions mapping")
    # admissions_map = {}
    # admissions_map.update({sample_symptom.hadm_id: sample_symptom.symptoms})
    # print(admissions_map)
    #
    # list_of_symptoms = sample_symptom.symptoms.split(",")
    #
    # print(list_of_symptoms)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
