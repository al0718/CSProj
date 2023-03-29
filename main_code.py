import pandas as pd
import numpy as nm
#Reads the csv with proper encoding. 
df = pd.read_csv('breastCancerWisconsin.csv', sep = ',', encoding='utf-8', encoding_errors='ignore')
#Deletes rows in the original DataFrame with missing cells. 
df.dropna(inplace = True)
#Calculates the mean, median, mode, variance, and standard deviation of the ClumpThick and ClassNum columns. 
clumpMean = df["ClumpThick"].mean()
classMean = df["ClassNum"].mean()
clumpMed = df["ClumpThick"].median()
classMed = df["ClassNum"].mean()
clumpMode = df["ClumpThick"].mode()
classMode = df["ClassNum"].mode()
clumpVar = df["ClumpThick"].var()
classVar = df["ClassNum"].var()
clumpStand = df["ClumpThick"].std()
classStand = df["ClassNum"].std()

print(clumpMean)
print(classMean)
print(clumpMed)
print(classMed)
print(clumpMode)
print(classMode)
print(clumpVar)
print(classVar)
print(clumpStand)
print(classStand)

#print(df.head(10))
print(df.to_string())
