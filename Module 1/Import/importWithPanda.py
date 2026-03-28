import pandas as pd

path = "archive.csv" #Define a variable name 'path' with the location of the file
df = pd.read_csv(path, header= None) #read_csv asume that the file contains a header, but we can ignore by using 'header = None'
print(df)

#print(df.head(n)) This will print n rows starting from the top
#print(df.tail(n)) And this one are gonna do the same but from the last one

#If we want to replace the header we can do the following actions:
headers = ["Alumno","Edad","Fecha de Nacimiento","Legajo","Grupo"] #Here we define the headers like a list of strings
df.columns = headers 
print(df)

path = "ExportFiles/newArchive.csv"
df.to_csv(path)