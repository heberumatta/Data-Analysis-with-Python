import pandas as pd
import numpy as np

path =  "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style","drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type","num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers

#replace the "?" with NaN
df.replace("?", np.nan, inplace=True)
missing_data = df.isnull()

# for column in missing_data.columns.values.tolist():
#     print(column)
#     print(missing_data[column].value_counts())
#     print("")

avg_normalized_losses = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_normalized_losses)

df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg_normalized_losses)
df["normalized-losses"] = df["normalized-losses"].astype("float")
print(df["normalized-losses"].head(20))
#papanga
