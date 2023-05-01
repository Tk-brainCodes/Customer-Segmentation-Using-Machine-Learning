import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("Mall_Customers.csv")

# drop the CustomerID column because it is not needed for the analysis
df.drop(["CustomerID"], axis=1, inplace=True)

# convert csv file to dictionary
data_dict = df.to_dict(orient='records')


class AnnualIncome:
    # to unserstand which range of customer group that has the hightest Annaul income
    # ai - as "annaul income"
    ai_0_30 = df["Annual Income (k$)"][(
        df["Annual Income (k$)"] >= 0) & (df["Annual Income (k$)"] <= 30)]
    ai_31_60 = df["Annual Income (k$)"][(
        df["Annual Income (k$)"] >= 31) & (df["Annual Income (k$)"] <= 60)]
    ai_91_120 = df["Annual Income (k$)"][(
        df["Annual Income (k$)"] >= 91) & (df["Annual Income (k$)"] <= 120)]
    ai_121_150 = df["Annual Income (k$)"][(
        df["Annual Income (k$)"] >= 121) & (df["Annual Income (k$)"] <= 150)]

    ai_x_axis = ["$ 0-30,000", "$ 31,000-60,000",
                 "$ 91,000-120,000", "$ 121,000-150,000"]
    ai_y_axis = [len(ai_0_30.values), len(ai_31_60.values),
                 len(ai_91_120.values), len(ai_121_150.values)]

    plt.figure(figsize=(15, 6))
    sns.barplot(x=ai_x_axis, y=ai_y_axis, palette="Spectral")
    plt.title("Annual Income")
    plt.xlabel("Income")
    plt.ylabel("Number of Customer")
    plt.show()
