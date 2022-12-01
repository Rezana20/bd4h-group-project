# This is a sample Python script.
import data_transformer
import cds
import metrics


def get_metrics():
    print("Module 5 print metrics")
    graphs = metrics.metrics()
    graphs.sketch()


def make_diagnosis():
    print("Module 4 cds diagnosis")

    diagnosis = cds.cds()

    diagnosis.search_fold("Fold0")


def data_ordering(data_trans):
    print("Module 3, vector ordering")

    # print("Fold0, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold0")
    # data_trans.rearrange(fold0_dictionary, "Fold0")
    #
    # print("Fold1, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold1")
    # data_trans.rearrange(fold0_dictionary, "Fold1")
    #
    # print("Fold2, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold2")
    # data_trans.rearrange(fold0_dictionary, "Fold2")
    #
    # print("Fold3, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold3")
    # data_trans.rearrange(fold0_dictionary, "Fold3")
    #
    # print("Fold4, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold4")
    # data_trans.rearrange(fold0_dictionary, "Fold4")
    #
    # print("Fold5, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold5")
    # data_trans.rearrange(fold0_dictionary, "Fold5")
    #
    # print("Fold6, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold6")
    # data_trans.rearrange(fold0_dictionary, "Fold6")
    #
    # print("Fold7, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold7")
    # data_trans.rearrange(fold0_dictionary, "Fold7")
    #
    # print("Fold8, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold8")
    # data_trans.rearrange(fold0_dictionary, "Fold8")
    #
    # print("Fold9, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold9")
    # data_trans.rearrange(fold0_dictionary, "Fold9")


def data_sorting(data_trans):
    print("Module 2, data pre-sorting")

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


def test_data_preprocessing(data_trans):
    print("Module 1, test data preprocessing")

    # print("Fold0 pre-processing.....")
    # data_trans.process_fold_data("Fold0", "TestSet")
    #
    # print("Fold1 pre-processing.....")
    # data_trans.process_fold_data("Fold1", "TestSet")
    #
    # print("Fold2 pre-processing.....")
    # data_trans.process_fold_data("Fold2", "TestSet")
    #
    # print("Fold3 pre-processing.....")
    # data_trans.process_fold_data("Fold3", "TestSet")
    #
    # print("Fold4 pre-processing.....")
    # data_trans.process_fold_data("Fold4", "TestSet")
    #
    # print("Fold5 pre-processing.....")
    # data_trans.process_fold_data("Fold5", "TestSet")
    #
    # print("Fold6 pre-processing.....")
    # data_trans.process_fold_data("Fold6", "TestSet")
    #
    # print("Fold7 pre-processing.....")
    # data_trans.process_fold_data("Fold7", "TestSet")
    #
    # print("Fold8 pre-processing.....")
    # data_trans.process_fold_data("Fold8", "TestSet")
    #
    # print("Fold9 pre-processing.....")
    # data_trans.process_fold_data("Fold9", "TestSet")


def data_preprocessing(data_trans):
    print("Module 1, training data pre-processing")

    # print("Fold0 pre-processing.....")
    # data_trans.process_fold_data("Fold0", "TrainingSet")
    #
    # print("Fold0 pre-processing.....")
    # data_trans.process_fold_data("Fold0", "TrainingSet")
    #
    # print("Fold1 pre-processing.....")
    # data_trans.process_fold_data("Fold1", "TrainingSet")
    #
    # print("Fold2 pre-processing.....")
    # data_trans.process_fold_data("Fold2", "TrainingSet")
    #
    # print("Fold3 pre-processing.....")
    # data_trans.process_fold_data("Fold3", "TrainingSet")
    #
    # print("Fold4 pre-processing.....")
    # data_trans.process_fold_data("Fold4", "TrainingSet")
    #
    # print("Fold5 pre-processing.....")
    # data_trans.process_fold_data("Fold5", "TrainingSet")
    #
    # print("Fold6 pre-processing.....")
    # data_trans.process_fold_data("Fold6", "TrainingSet")
    #
    # print("Fold7 pre-processing.....")
    # data_trans.process_fold_data("Fold7", "TrainingSet")
    #
    # print("Fold8 pre-processing.....")
    # data_trans.process_fold_data("Fold8", "TrainingSet")
    #
    # print("Fold9 pre-processing.....")
    # data_trans.process_fold_data("Fold9", "TrainingSet")


if __name__ == '__main__':
    data_trans = data_transformer.data_transformer()

    # data_preprocessing(data_trans)

    # test_data_preprocessing(data_trans)

    # data_sorting(data_trans)

    # data_ordering(data_trans)

    # make_diagnosis()

    # get_metrics()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
