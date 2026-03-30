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

#If you want to see a specific column, you can use the following code:
#df['column_name'] #this will show the specified column of the data frame
print(df[0]) #this will show the first column of the data frame

#Data Cleaning | Data preprocessing | Data Wrangling
#The process of converting or mapping data from the initial "raw" dorm into another format,
#in order to prepare the data for further analysis.