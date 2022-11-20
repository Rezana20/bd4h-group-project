# class to perform our metrics
import csv
import pandas as pd
import matplotlib.pyplot as plt

class metrics:

    def __init__(self):
        print("init")  # never prints

    def sketch(self):
        # read dictionary
        precision_dict = self.read_dict()
        average_precision_list = []

        df = pd.DataFrame()

        for test_keys in precision_dict.keys():
            clean_value = precision_dict[test_keys].lstrip("[").rstrip("]")
            clean_value_list = clean_value.split(",")

            A = [float(x) for x in clean_value_list]
            df = df.append(pd.DataFrame([A]))

        average_precision_list = [df[0].mean(), df[1].mean(), df[2].mean(), df[3].mean(), df[4].mean(), df[5].mean(), df[6].mean()]

        plt.figure(figsize=(9, 6))
        plt.plot([1,5,10,15,20,25,30],average_precision_list)
        plt.title("Average precision over alphas")
        plt.xlabel("Top K")
        plt.ylabel("Precison")
        plt.savefig("average_precision.png")

        # compute average

        # build graph

    def read_dict(self):
        folder_path = "./data/ordered/Fold0"
        folder = folder_path + "/precisionFold0.csv"

        with open(folder) as csv_file:
            reader = csv.reader(csv_file)
            precision = dict(reader)

            return precision

            close()
