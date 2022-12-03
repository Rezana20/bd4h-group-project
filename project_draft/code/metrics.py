# class to perform our metrics
import csv
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d


class metrics:

    def __init__(self):
        print("init")  # never prints

    def sketch_precision(self):

        print("Calculating the Precision = TP / (TP+FP)")
        print("False Positives is the mistakenly diagnosed ground truths")

        # Fold 1 for 0.7
        # TP, "[1, 1, 1, 3, 4, 5, 5]" reference TP_TNFold1_0.7.csv

        # Fold 5 for 0.7
        # TP, "[3, 3, 4, 4, 4, 4, 5]" reference TP_TNFold1_0.7.csv

        # Fold 6 for 0.8 TP_TNFold6_0.8.csv
        # TP, "[2, 2, 2, 2, 2, 4, 4]" reference TP_TNFold6_0.8.csv

        # Fold 8 for 0.8 TP_TNFold6_0.8.csv
        # TP, "[2, 2, 2, 2, 3, 4, 4]" reference TP_TNFold8_0.8.csv

        # Fold 3 for 0.9 TP_TNFold3_0.9.csv
        # TP,"[1, 1, 2, 2, 2, 2, 3]" reference TP_TNFold3_0.9.csv

        # Fold 0 for 0.9 TP_TNFold0_0.9.csv
        # TP, "[1, 1, 1, 1, 1, 2, 2]" reference TP_TNFold0_0.9.csv

        # Average from each selected fold
        TP_0_7 = [2, 2, 2.5, 3.5, 4, 4.5, 5]
        TP_0_8 = [2, 2, 2, 2, 2.5, 4, 4]
        TP_0_9 = [1, 1, 1.5, 1.5, 1.5, 2, 2.5]

        # average_precision_list_07 = [0.15, 0.15, 0.19, 0.27, 0.30, 0.37, 0.38]

        # Precision Calculation
        precision_0_7 = [0.25, 0.25, 0.31, 0.44, 0.5, 0.56, 0.63]
        precision_0_8 = [0.25, 0.25, 0.25, 0.25, 0.31, 0.5, 0.5]
        precision_0_9 = [0.13, 0.13, 0.19, 0.19, 0.19, 0.25, 0.31]

        # Precision Graph
        x = [1, 5, 10, 15, 20, 25, 30]
        y_0_7 = gaussian_filter1d(precision_0_7, sigma=2)
        y_0_8 = gaussian_filter1d(precision_0_8, sigma=2)
        y_0_9 = gaussian_filter1d(precision_0_9, sigma=2)
        plt.figure(figsize=(9, 6))
        plt.plot(x, y_0_7, label="0.70")
        plt.plot(x, y_0_8, label="0.80")
        plt.plot(x, y_0_9, label="0.90")
        plt.title("Average precision over alphas")
        plt.xlabel("Top K")
        plt.ylabel("Precision")
        plt.legend()
        plt.savefig("average_precision.png")

    def sketch_recall(self):
        print("Calculating the Recall = TP / (TP+TN)")
        print("TP + TN is considered the total number of tests in each fold of data.")

        TP_0_7 = [2, 2, 2.5, 3.5, 4, 4.5, 5]
        TP_0_8 = [2, 2, 2, 2, 2.5, 4, 4]
        TP_0_9 = [1, 1, 1.5, 1.5, 1.5, 2, 2.5]
        TP_and_TN = [13, 13, 13, 13, 13, 13, 13]

        recall_0_7 = [0.15, 0.15, 0.19, 0.27, 0.30, 0.37, 0.38]
        recall_0_8 = [0.15, 0.15, 0.15, 0.15, 0.19, 0.3, 0.3]
        recall_0_9 = [0.08, 0.08, 0.12, 0.12, 0.12, 0.15, 0.19]
        x = [1, 5, 10, 15, 20, 25, 30]
        plt.figure(figsize=(9, 6))
        y_0_7 = gaussian_filter1d(recall_0_7, sigma=2)
        y_0_8 = gaussian_filter1d(recall_0_8, sigma=2)
        y_0_9 = gaussian_filter1d(recall_0_9, sigma=2)
        plt.plot(x, y_0_7, label="0.70")
        plt.plot(x, y_0_8, label="0.80")
        plt.plot(x, y_0_9, label="0.90")
        plt.title("Average recall over alphas")
        plt.xlabel("Top K")
        plt.ylabel("Recall")
        plt.legend()
        plt.savefig("average_recall.png")

    def read_dict(self):
        folder_path = "./data/ordered/Fold0"
        folder = folder_path + "/precisionFold0.csv"

        with open(folder) as csv_file:
            reader = csv.reader(csv_file)
            precision = dict(reader)

            return precision

            close()

# We are attempting to calculate top k (30)
# Fold 0....
# Execution time: 813.1151769161224 seconds
# We are attempting to calculate top k (30)
# Fold 1....
# Execution time: 3795.3196308612823 seconds
# We are attempting to calculate top k (30)
# Fold 2....
# cExecution time: 4037.3273248672485 seconds
# We are attempting to calculate top k (30)
# Fold 3....
# Execution time: 4472.14191198349 seconds
# We are attempting to calculate top k (30)
# Fold 4....
# Execution time: 22710.0295920372 seconds
# We are attempting to calculate top k (30)
# Fold 5....
# Execution time: 12652.455038070679 seconds
# We are attempting to calculate top k (30)
# Fold 6....
# Execution time: 3069.5184009075165 seconds
# We are attempting to calculate top k (30)
# Fold 7....
# Execution time: 1246.1353962421417 seconds
# We are attempting to calculate top k (30)
# Fold 8....
# Execution time: 992.1770920753479 seconds
# We are attempting to calculate top k (30)
# Fold 9....
# Execution time: 809.9623980522156 seconds
