import pandas as pd
import numpy as np

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(path, header=None)

#Question 1:
#print("The bottom 10 rows of data frame 'df':\n")
#print(df.tail(10))

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style","drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type","num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
#print(df.head(10))

#We neew to replace '?' symbol for NaN
df1 = df.replace('?',np.nan)
#print(df1.head(10))

df = df1.dropna(subset=["price"], axis=0)
#print(df.head(10))

#Question 2: find headers name
#print(df.columns)

#NOTE: if we use to_csv(), for eg: df.to_csv(path, index = False) with this index = False means the rows names will not be written
#df.to_csv("automobile.csv", index = False) 

#df.dtypes() with this a series with the data types of each column is returned

#If we would like to get a statistical summary of each column e.g. count, column mean value, column standard deviation, etc., we use the describe method:
#print(df.describe())
#we can also add include = "all"
#print(df.describe(include = "all"))

#Question 3: Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.
print(df[['length', 'compression-ratio']].describe())