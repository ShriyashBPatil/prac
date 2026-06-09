import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
import matplotlib.pyplot as plt
df=pd.read_csv("Play Tennis.csv")
X=df.iloc[:,1:-1]
x_col=X.columns
ohe=OneHotEncoder(drop='first')
X=ohe.fit_transform(X)
feature_names=ohe.get_feature_names_out(x_col)
y=df.iloc[:,-1]
le=LabelEncoder()
y=le.fit_transform(y)
clf= DecisionTreeClassifier(random_state=0)
clf.fit(X,y)
plt.figure(figsize=(14,8))
plot_tree(clf,
          feature_names=feature_names,
          class_names=['Yes','No'],
          filled=True
         )
plt.show()
