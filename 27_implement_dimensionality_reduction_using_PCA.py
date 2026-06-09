from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
digits = load_digits()
X = digits.data
y = digits.target
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
print(pca.explained_variance_ratio_)
plt.figure(figsize=(8,6))
scatter = plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=y
)
plt.title("PCA")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.colorbar(scatter)
plt.show()
