from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
df = pd.read_csv("Social_Network_Ads.csv")
X = df.iloc[:, [2,3]]
y = df.iloc[:, 4]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train, y_train)
print(svm.predict(sc.transform([[30,87000]])))
y_pred = svm.predict(X_test)
confusionMatrix = confusion_matrix(y_test, y_pred)
print(confusionMatrix)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
