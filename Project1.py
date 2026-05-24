import pandas as pd

#TASK 1 
df = pd.read_csv('loan.csv')
df.head()      #Gives initial 5 rows of the dataset
df.info()      #Gives the summary of the dataset, including data types and non-null counts
df.describe()  #Provides statistical summary of numerical columns in the dataset

#TASK 2
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

