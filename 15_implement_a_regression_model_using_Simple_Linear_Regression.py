import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,mean_absolute_error
df=pd.read_csv("Salary_dataset.csv")
print(df.head(3))
X=df.iloc[:,1:2]
y=df.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title("salary vs experience")
plt.xlabel("salary")
plt.ylabel("exp")
plt.show()
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title("salary vs experience")
plt.xlabel("salary")
plt.ylabel("exp")
plt.show()
print("if person has 4 year of exp what would be slaary:")
print(regressor.predict([[4]]))
print("regression coeffiecient:",regressor.coef_)
print("regression intercept:",regressor.intercept_)

meansquarederror=mean_squared_error(y_test,y_pred)
print("meansquarederror:",meansquarederror)
meanabsoluteerror=mean_absolute_error(y_test,y_pred)
print("meanabsoluteerror:",meanabsoluteerror)
