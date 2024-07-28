from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
import pandas as pd
df=pd.read_csv("iris.csv")
print(df.head(5))
df['Species'].value_counts()
x=df.drop(['Id','Species'],axis=1)
y=df['Species']
print(x.head(5))
print(y.head(5))
train_x,test_x,train_y,test_y=train_test_split(x,y,train_size=0.8,random_state=80)
knn=KNeighborsClassifier(n_neighbors=5)
print(knn.fit(train_x,train_y))
print(knn.score(test_x,test_y))
