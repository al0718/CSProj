import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Reads the csv with proper encoding. Python will now automatically read all the datapoints, using pandas. 
df = pd.read_csv('breastCancerWisconsin.csv', sep = ',', encoding='utf-8', encoding_errors='ignore')
#Deletes rows in the original DataFrame with missing cells in any of the columns. The inplace = true makes it so that adjustment is done to the original DataFrame and a copy is not required. 
df.dropna(inplace = True)
#Calculates the mean, median, mode, variance, and standard deviation of the ClumpThick and ClassNum columns. This is done using the applicable built in funtion (ex: .mean() or .mode()). Each value is saved into a varaible so it can be printed later. 
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
'''
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

#This prints all of the values in the DataFrame as a string, set up like a table. 
print(df.to_string())
'''
#This will be used to make a pie chart. 
df1 = df.groupby(['ClassNum'])['ClassNum'].count()
print(df1)
#This will be used to make a bar graph. 
df2 = df.groupby(['BlandChromatin'])['BlandChromatin'].count()
print(df2)
x_2 = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
y_2 = np.array([150, 159, 161, 39, 34, 9, 71, 28, 11, 20])
x_2_label = "Number of Patients"
y_2_label = "Bland Chromatin Amount"
plt.bar(x_2,y_2, labels = x_2_label)
plt.show()
