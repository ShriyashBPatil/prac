from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
X = np.array([
    [4,13],
    [5,17],
    [8,27],
    [2,23],
    [11,25],
    [13,26],
    [3,29],
    [2,30],
    [12,24],
    [4,22]
])
cluster = AgglomerativeClustering(
    n_clusters=2,
    linkage='ward'
)
labels = cluster.fit_predict(X)
plt.scatter(
    X[:,0],
    X[:,1],
    c=labels,
    cmap='rainbow'
)
plt.title("Agglomerative Clustering")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()
