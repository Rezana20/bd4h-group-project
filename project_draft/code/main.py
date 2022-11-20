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
    print("Module 3, searching for best match based")

    # print("Fold0, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold0")
    # data_trans.rearrange(fold0_dictionary, "Fold0")

    # print("Fold1, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold1")
    # data_trans.rearrange(fold0_dictionary, "Fold1")

    # print("Fold2, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold2")
    # data_trans.rearrange(fold0_dictionary, "Fold2")

    # print("Fold3, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold3")
    # data_trans.rearrange(fold0_dictionary, "Fold3")

    # print("Fold4, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold4")
    # data_trans.rearrange(fold0_dictionary, "Fold4")

    # print("Fold5, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold5")
    # data_trans.rearrange(fold0_dictionary, "Fold5")

    # print("Fold6, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold6")
    # data_trans.rearrange(fold0_dictionary, "Fold6")

    # print("Fold7, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold7")
    # data_trans.rearrange(fold0_dictionary, "Fold7")

    # print("Fold8, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold8")
    # data_trans.rearrange(fold0_dictionary, "Fold8")

    # print("Fold9, order sorted file.........")
    # fold0_dictionary = data_trans.fetch_sorted_data("Fold9")
    # data_trans.rearrange(fold0_dictionary, "Fold9")


def data_sorting(data_trans):
    print("Module 2, data pre-sorting")

    # print("Fold0 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold0")

    # print("Fold1 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold1")

    # print("Fold2 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold2")

    # print("Fold3 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold3")

    # print("Fold4 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold4")

    # print("Fold5 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold5")

    # print("Fold6 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold6")

    # print("Fold7 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold7")

    # print("Fold8 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold8")

    # print("Fold9 sorting.....")
    # data_trans.fetch_processed_data_fold("Fold9")


def data_preprocessing(data_trans):
    print("Module 1, data pre-processing")

    # print("Fold0 pre-processing.....")
    # data_trans.read_fold("Fold0")

    # print("Fold0 pre-processing.....")
    # data_trans.read_fold("Fold0")

    # print("Fold1 pre-processing.....")
    # data_trans.read_fold("Fold1")

    # print("Fold2 pre-processing.....")
    # data_trans.read_fold("Fold2")

    # print("Fold3 pre-processing.....")
    # data_trans.read_fold("Fold3")

    # print("Fold4 pre-processing.....")
    # data_trans.read_fold("Fold4")

    # print("Fold5 pre-processing.....")
    # data_trans.read_fold("Fold5")

    # print("Fold6 pre-processing.....")
    # data_trans.read_fold("Fold6")

    # print("Fold7 pre-processing.....")
    # data_trans.read_fold("Fold7")

    # print("Fold8 pre-processing.....")
    # data_trans.read_fold("Fold8")

    # print("Fold9 pre-processing.....")
    # data_trans.read_fold("Fold9")


if __name__ == '__main__':
    data_trans = data_transformer.data_transformer()

    # data_preprocessing(data_trans)

    # data_sorting(data_trans)

    # data_ordering(data_trans)

    # make_diagnosis()

    get_metrics()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
