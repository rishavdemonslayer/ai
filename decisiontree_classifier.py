import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv("")#csv file
x=df.drop(['Result'],axis=1)
y=df['Result']
train_x,test_x,train_y,test_y=train_test_split(x,y,train_size=0.2,random_state=100)
estimated=DecisionTreeClassifier().fit(train_x,train_y)
predict_y=estimated.predict(test_x)
print(predict_y)
print(accuracy_score(test_y,predict_y))