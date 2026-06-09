import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
df=pd.read_csv("Social_Network_Ads.csv")
print(df.head(2))
X=df[['Gender','Age','EstimatedSalary']]
y=df['Purchased']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
ct=ColumnTransformer(
    transformers=[
        ('cat',OneHotEncoder(drop='first'),['Gender']),
        ('num',StandardScaler(),['Age','EstimatedSalary'])
    ])
X_train=ct.fit_transform(X_train)
X_test=ct.transform(X_test)
model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
confusionmatrix=confusion_matrix(y_test,y_pred)
print("confusionmatrix:",confusionmatrix)
accuracy=accuracy_score(y_test,y_pred)
print("accuracy:",accuracy)
