import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


df = pd.read_csv("Mall_Customers.csv")

# drop the CustomerID column because it is not needed for the analysis
df.drop(["CustomerID"], axis=1, inplace=True)

# convert csv file to dictionary
data_dict = df.to_dict(orient='records')


plt.figure(1, figsize=(15, 7))
n = 0


class ViolinplotDistribution:
    # A violin plot that shows the distribution of age, annaul income and spending score based on gender
    for cols in ['Age', 'Annual Income (k$)', 'Spending Score (1-100) ']:
        n += 1
        plt.subplot(1, 3, n)
        sns.set(style="whitegrid")
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.violinplot(x=cols, y='Gender', data=df)
        plt.ylabel('Gender' if n == 1 else '')
        plt.title("Violinplot")
    plt.show()
