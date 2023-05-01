import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("Mall_Customers.csv")

# drop the CustomerID column because it is not needed for the analysis
df.drop(["CustomerID"], axis=1, inplace=True)

# convert csv file to dictionary
data_dict = df.to_dict(orient='records')


class HighestSpendingScore:
    # to unserstand which range of customer group has the hightest spending score
    # ss - as "spending score"
    ss_1_20 = df["Spending Score (1-100) "][(df["Spending Score (1-100) "]
                                            >= 1) & (df["Spending Score (1-100) "] <= 20)]
    ss_21_40 = df["Spending Score (1-100) "][(df["Spending Score (1-100) "]
                                              >= 21) & (df["Spending Score (1-100) "] <= 40)]
    ss_61_80 = df["Spending Score (1-100) "][(df["Spending Score (1-100) "]
                                              >= 61) & (df["Spending Score (1-100) "] <= 80)]
    ss_81_100 = df["Spending Score (1-100) "][(df["Spending Score (1-100) "]
                                               >= 81) & (df["Spending Score (1-100) "] <= 100)]

    ss_x_axis = ["1-20", "21-40", "61-80", "81-100"]
    ss_y_axis = [len(ss_1_20.values), len(ss_21_40.values),
                 len(ss_61_80.values), len(ss_81_100.values)]

    plt.figure(figsize=(15, 6))
    sns.barplot(x=ss_x_axis, y=ss_y_axis, palette="rocket")
    plt.title("Spending Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Customer Having the Score")
    plt.show()
