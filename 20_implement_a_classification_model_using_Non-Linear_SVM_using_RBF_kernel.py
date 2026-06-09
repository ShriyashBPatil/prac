from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.datasets import make_circles
X, y = make_circles(
    n_samples=500,
    factor=0.5,
    noise=0.05,
    random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
svm = SVC(
    kernel='rbf',
    C=1,
    gamma=0.5
)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
confusionMatrix = confusion_matrix(y_test, y_pred)
print(confusionMatrix)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
