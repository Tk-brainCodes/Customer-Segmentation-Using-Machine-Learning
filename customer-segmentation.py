import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from clusters_age_ss import ClusterBetweenAgeAndSpendingScore
from relationship_age_spendingScore import AnnualIncome
from range_of_high_annaulIncome import HighestSpendingScore
from range_of_customers import HighestCustomer
from violinplot_distribution import ViolinplotDistribution
from distribution import Distribution

df = pd.read_csv("Mall_Customers.csv")

# drop the CustomerID column because it is not needed for the analysis
df.drop(["CustomerID"], axis=1, inplace=True)

ageAndSpendingScore = HighestSpendingScore()
clusterAgeSpedingScore = ClusterBetweenAgeAndSpendingScore()
annaulIncome = AnnualIncome()
rangeOfCustomers = HighestCustomer()
distributionViolinplot = ViolinplotDistribution()
distributionData = Distribution()


# form clusters based on annual income and spending scores
X2 = df.loc[:, ["Annual Income (k$)", "Spending Score (1-100) "]].values

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init="k-means++")
    kmeans.fit(X2)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(12, 6))
plt.grid()
plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
plt.xlabel("K Value")
plt.ylabel("WCSS")

kmeans = KMeans(n_clusters=5)
label = kmeans.fit_predict(X2)
# cluster centriod
kmeans.cluster_centers_

plt.scatter(X2[:, 0], X2[:, 1], c=kmeans.labels_, cmap="rainbow")
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1], color="black")
plt.title("Clusters of Customers")
plt.xlabel("Annaual Income (k$)")
plt.ylabel("Spending Score(1-100) ")
plt.show()

# # form clusters based on annual income, age, and spending scores
# X3 = df.iloc[:, 1:]

# wcss = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k, init="k-means++")
#     kmeans.fit(X3)
#     wcss.append(kmeans.inertia_)
# plt.figure(figsize=(12, 6))
# plt.grid()
# plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
# plt.xlabel("K Value")
# plt.ylabel("WCSS")

# kmeans = KMeans(n_clusters=5)
# clusters = kmeans.fit_predict(X3)
# # cluster centriod
# kmeans.cluster_centers_

# df["label"] = clusters

# fig = plt.figure(figsize=(20, 10))
# ax = fig.add_subplot(111, projection="3d")
# ax.scatter(df.Age[df.label == 0], df["Annual Income (k$)"][df.label == 0],
#            df["Spending Score (1-100) "][df.label == 0], c="blue", s=60)
# ax.scatter(df.Age[df.label == 1], df["Annual Income (k$)"][df.label == 0],
#            df["Spending Score (1-100) "][df.label == 1], c="red", s=60)
# ax.scatter(df.Age[df.label == 2], df["Annual Income (k$)"][df.label == 0],
#            df["Spending Score (1-100) "][df.label == 2], c="green", s=60)
# ax.scatter(df.Age[df.label == 3], df["Annual Income (k$)"][df.label == 0],
#            df["Spending Score (1-100) "][df.label == 3], c="orange", s=60)
# ax.scatter(df.Age[df.label == 4], df["Annual Income (k$)"][df.label == 0],
#            df["Spending Score (1-100) "][df.label == 4], c="purple", s=60)


# ax.view_init(30, 185)
# plt.xlabel("Age")
# plt.ylabel("Annaul Income (k$)")
# ax.set_zlabel("Spending Score (1-100) ")
# plt.show()

# print(df.head())
# print(df.shape)
# print(df.describe())
# print(df.dtypes)
# print(df.isnull().sum())
