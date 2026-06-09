import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model saved successfully")
with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
print("Model loaded successfully")
y_pred = loaded_model.predict(X_test)
confusionMatrix = confusion_matrix(y_test, y_pred)
print(confusionMatrix)
