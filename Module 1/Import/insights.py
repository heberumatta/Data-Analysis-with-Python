import pandas as pd

path = "ExportFiles/newArchive.csv"
df = pd.read_csv(path) #df = dataframe

print(df.dtypes) #this will print the data types in a row

#print(df.describe())
#print(df.describe(include = "all"))

print(df.info())