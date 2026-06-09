import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
df=pd.read_csv("Social_Network_Ads.csv")
X=df.iloc[:,[2,3]]
y=df.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
forest=RandomForestClassifier(n_estimators=5,criterion='gini',random_state=42)
forest.fit(X_train,y_train)
y_pred=forest.predict(X_test)
tree_model=forest.estimators_[3]
plt.figure(figsize=(12,8))
plot_tree(tree_model,
          feature_names=['Age','EstimatedSalary'],
          class_names=['no','yes'],
          filled=True
         )
plt.show()
