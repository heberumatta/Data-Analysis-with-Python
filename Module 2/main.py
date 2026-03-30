#Data Cleaning | Data preprocessing | Data Wrangling
#The process of converting or mapping data from the initial "raw" dorm into another format,
#in order to prepare the data for further analysis.
#Learning Objectives
#   Identify and handle missing values
#   Data formatting
#   Data normalization (centering and scaling)
#   Data Binning
#   Turning categorical values to numeric variables

#Importing libraries
import pandas as pd
import numpy as np

#Importing the dataset
path = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style","drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type","num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers

#If you want to see a specific column, you can use the following code:
#df['column_name'] #this will show the specified column of the data frame
#df["price"] #this will show the first column of the data frame

#Dealing with missing values
#Missing values occur when no data value is stored for the variable in an observation.
#They can be represented as NaN, NULL, ?, 0 or simply a blank cell.
#How to deal with missung data?
#1. check with the data collection source
#2. Drop the missing values
#3. Replace the missing values with some other value (mean, median, mode, etc.)
#4. Leave the missing values as they are (if the analysis method can handle them)

# Use: dataframes.dropna() to drop the missing values
#   You need to specify the axis (0 for rows, 1 for columns) and the how parameter (any or all)
#   inplace=True will modify the original dataframe, if False it will return a new dataframe with the missing values dropped
#   Example: df.dropna(subset=["price"], axis=0, inplace=True)
# Use: dataframe.replace() to replace the missing values with some other value
#   You need to specify the to_replace parameter (the value to be replaced) and the value parameter (the value to replace with)
#   Example: df.replace(missing_value, new_value)
#   To replace if we want to calculate the mean, median or mode of a column, we can use the following code:
#   mean = df[column_name].mean()

# df.dropna(subset=["price"], axis=0, inplace=True)
# mean_price = df["price"].mean()
# df.replace('?', mean_price, inplace=True)

#Data formatting
#Data are usually collected from different places and stored in different formats.
#Bringing data into a common standard of expression allows users to make meaningful comparison.

#Applying calculations to an entire column
#For example, if we wantr to convert "mpg" to "L/100km", we can use the following code:
#df[mpg_column] = 235 / df[mpg_column] We use just one line of code
#The you can rename the column to "L/100km" using the following code: 
#df.rename(columns={mpg_column: "L/100km"}, inplace=True)

#When we apliy calculations there can be incorrect data types, we can use the following code to change the data type of a column:
# df["price"] = df["price"].astype("float")

#Binning: grouping values into bins, convert numeric into categorical variables, group a set numerical values into a set of "bins".
#First, we use the numpy function linspace() to return the array bins.
# bins = np.linspace(min(df["price"]), max(df["price"]), 4)
# group_names = ["Low", "Medium", "High"]
# df["price_binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)

#Turning categorical values to numeric variables
# Use pandas.get_dummies() to convert categorical variables into dummy/indicator variables
# Example:
df = pd.get_dummies(df, columns=["fuel-type"])
print(df[["fuel-type_diesel", "fuel-type_gas"]].head(10))
#now to convert both columns into one column we can use the following code:
#My code

df["price"] = df["price"].replace("?", np.nan)
df.dropna(subset=["price"], axis=0, inplace=True, how="all")

df["price"] = df["price"].astype("float")
#print(df["price"])

#To covert the price USD to pesos:
df["price"] = df["price"]*1500
df.rename(columns={"price": "price_pesos"}, inplace=True)

bins = np.linspace(min(df["price_pesos"]), max(df["price_pesos"]), 4)
goup_names = ["Low", "Medium", "High"]
df["price_binned"] = pd.cut(df["price_pesos"], bins, labels=goup_names, include_lowest=True)
#Explanation: we are creating a new column called "price_binned" and we are using the pd.cut() function to bin the
#"price_pesos" column into 3 bins (Low, Medium, High) based on the values of the "price_pesos" column. The bins are 
#created using the np.linspace() function which creates an array of equally spaced values between the minimum and
#maximum values of the "price_pesos" column. The include_lowest=True parameter is used to include the lowest value in the first bin.
#print(df[["price_pesos", "price_binned"]].head(20))

