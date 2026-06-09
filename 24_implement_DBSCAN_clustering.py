from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
X, y = make_moons(
    n_samples=300,
    noise=0.05,
    random_state=42
)
dbscan = DBSCAN(eps=0.2, min_samples=5)
clusters = dbscan.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=clusters)
plt.title("DBSCAN")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()
