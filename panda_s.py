import pandas as pd

#Building a data frame
sample_dataframe_df= pd.read_csv("Iris.csv")

#type of the generated file
print(type(sample_dataframe_df))

#Display first few entries in the data frame
pd.set_option('display.max_columns',5)
print(sample_dataframe_df.head(5))

#Getting summary of data frame
print(sample_dataframe_df.columns)

#Transpose operations on data frame
print(sample_dataframe_df.head(5).transpose())

#Finding the dimension of data set
print(sample_dataframe_df.shape)

#Slicing the data
print(sample_dataframe_df[0:10])

#To retrieve the last five data’s in the data set
print(sample_dataframe_df[-5:])

#To retrieve particular column from the data set
print(sample_dataframe_df['SepalLengthCm'])

#Occurrence of each unique value
print(sample_dataframe_df.Species.value_counts())

#Record Filter
print(sample_dataframe_df[sample_dataframe_df['SepalLengthCm']>1])

#Removing a particular row/column
print(sample_dataframe_df.drop('Id',inplace=True,axis=1))
print(list(sample_dataframe_df.columns))