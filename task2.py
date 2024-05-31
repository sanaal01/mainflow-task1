import pandas as pd
data=pd.read_csv("01.Data Cleaning and Preprocessing.csv")
#Intial and botom 5 rows
print("Intial and botom 5 rows")
print(data.head(5))


print("Printing the info of data")
print(data.info())
print("\n")
print("Printing the count of Null values in the particular Columns")
print(data.isnull().sum())
print("\n")
print("Total number of null values in whole dataset: ",data.isnull().sum().sum())
print("\n Data after dropping out the Duplicate values:")
data.drop_duplicates(inplace=True)
print(data)


#Performing Basic Statistics upon Dataset
""" Removing the unnecessary columns: """
print("\n Removing the unnecessary columns: ")
data.drop(columns="Observation",inplace=True)
print(data)

# Calculating Stats upon Dataset
print("\n Calculating Stats upon Dataset")
print(data.describe())