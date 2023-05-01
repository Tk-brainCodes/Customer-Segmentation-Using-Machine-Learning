import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("Mall_Customers.csv")

# drop the CustomerID column because it is not needed for the analysis
df.drop(["CustomerID"], axis=1, inplace=True)

# convert csv file to dictionary
data_dict = df.to_dict(orient='records')


class HighestCustomer:
    # divide the age into different categories,
    age_18_25 = df.Age[(df.Age >= 18) & (df.Age <= 25)]
    age_26_35 = df.Age[(df.Age >= 26) & (df.Age <= 35)]
    age_36_45 = df.Age[(df.Age >= 36) & (df.Age <= 45)]
    age_46_55 = df.Age[(df.Age >= 46) & (df.Age <= 55)]
    age_55above = df.Age[df.Age >= 56]

    age_x_axis = ["18-25", "26-35", "36-45", "46-55", "55+"]
    age_y_axis = [len(age_18_25.values), len(age_26_35.values), len(
        age_36_45.values), len(age_46_55.values), len(age_55above.values)]

    # to understand which range of age group that has the highest number of customers using the bar plot
    plt.figure(figsize=(15, 6))
    sns.barplot(x=age_x_axis, y=age_y_axis, palette="mako")
    plt.title("Number of Customers and Ages")
    plt.xlabel("Age")
    plt.ylabel("Number of Customers")

    # replot for annaul income and spending score
    sns.relplot(x="Annual Income (k$)", y="Spending Score (1-100) ", data=df)
    plt.show()
