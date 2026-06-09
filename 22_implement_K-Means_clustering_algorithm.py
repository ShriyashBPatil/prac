import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:, :2]
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centroids = kmeans.cluster_centers_
print("Centroids:", centroids)
plt.scatter(
    X[:,0],
    X[:,1],
    c=y_kmeans
)
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    s=200,
    marker='X'
)
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()
