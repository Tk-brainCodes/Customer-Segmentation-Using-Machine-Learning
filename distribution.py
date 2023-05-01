import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


df = pd.read_csv("Mall_Customers.csv")

# drop the CustomerID column because it is not needed for the analysis
df.drop(["CustomerID"], axis=1, inplace=True)
# convert csv file to dictionary
data_dict = df.to_dict(orient='records')
plt.figure(1, figsize=(15, 6))
n = 0


class Distribution:
    # shows the distribution of age, annual income and spending score
    for x in ['Age', 'Annual Income (k$)', 'Spending Score (1-100) ']:
        n += 1
        plt.subplot(1, 3, n)  # represents the number of rows ans columns
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.displot(df[x], bins=20)
        plt.title("Displot of {}".format(x))
    plt.show()
