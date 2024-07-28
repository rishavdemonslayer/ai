import pandas as pd 
import numpy as np
dates = pd.date_range('20230101', periods=6)
# series 
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# dataframe from numpy array
df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df1)

#creating dataframe using list
my_list = [[1,2,3],
           [4,5,6],
           [7,8,9],
           [10,11,12],
           [13,14,15]]


df = pd.DataFrame(my_list)

# from Dictionary 
students = {
    'name' : ['AAAAA', 'BBBBBB', 'CCCCCC'],
    'Age' : [23, 22, 21],
    'Reg' : ['20AA2192', '21BB3131', '21CC4253']
}
df = pd.DataFrame(students)
#dictionary and numpy
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

#reading a csv or excel file
my_df=pd.read_csv("heights.csv")
print(my_df)
print(my_df.head(5))
print(my_df.tail(5))

print("description")
print(my_df.describe())
print("transpose of dataframe is")
print(my_df.T)

print(my_df.index)
print(my_df.columns)

my_df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(my_df2.columns)
print(my_df2.dtypes)
print(my_df2.to_numpy())

my_df['height']

my_df[0:3]

