import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("Mall_Customers.csv")

# drop the CustomerID column because it is not needed for the analysis
df.drop(["CustomerID"], axis=1, inplace=True)


# find the relationship between the "age" and "spending score"
# then cluster the data using KMeans clustering algorithm
X1 = df.loc[:, ["Age", "Spending Score (1-100) "]].values

wcss = []

class ClusterBetweenAgeAndSpendingScore:
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, init="k-means++")
        kmeans.fit(X1)
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(12, 6))
    plt.grid()
    plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
    plt.xlabel("K Value")
    plt.ylabel("WCSS")

    # number of clusters
    kmeans = KMeans(n_clusters=4)
    # centriods
    label = kmeans.fit_predict(X1)

    plt.scatter(X1[:, 0], X1[:, 1], c=kmeans.labels_, cmap="rainbow")
    plt.scatter(kmeans.cluster_centers_[:, 0],
                kmeans.cluster_centers_[:, 1], color="black")
    plt.title("Clusters of Customers")
    plt.xlabel("Age")
    plt.ylabel("Spending Score(1-100) ")
    plt.show()
