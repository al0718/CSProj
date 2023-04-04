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
#This function will go through each x and y value and add a label directly above each bar, plot, etc.
def addlabels(x,y):
    for i in range(len(x)):
        #The ha = center formats it to the center of each mark. The font is adjusted using the fontdict. The other values relate to the printing and the centering of the values. 
        plt.text(i, y[i]//2, y[i], ha = 'center', fontdict = value_font)

#These values will save the various fonts used throughout the graphs. 
title_font = {'family':'serif','weight':'bold','size':18 }
small_font = {'family':'serif','weight':'bold','size':12 }
value_font = {'family':'arial','weight':'bold','size':10 }

#The following counts the amount of patients at each class of breast cancer and groups them by class. This will be used to make a pie chart. 
df1 = df.groupby(['ClassNum'])['ClassNum'].count()
print(df1)
#The x_1 variable will create a Numpy array containing the different classes of breast cancer found in the pool of patients, or the x-values. 
x_1 = ['Class 2','Class 4']
#The y_1 variable will create a Numpy array contianing the amount of patients at each class of breast cancer, or the y-values. 
y_1 = np.array([443, 239])
#The following sets the bar graph to a specific size using the figure() function. 
plt.figure(figsize = (10, 5))
#This adds a title to the bar graph. 
plt.title('Number of Patients per Class of Breast Cancer', fontdict = title_font)
#This saves the pie chart as a variable so edits (like legends, axis titles, etc.) can be made. It also adds percentages to be displayed on each wedge.
pie = plt.pie(y_1, labels = x_1, autopct='%.1f%%',
    #This adjusts the style by adding a line between each wedge to make things more clear and by changing the font of the labels. 
    wedgeprops = {'linewidth': 3.0, 'edgecolor': 'white'},
    textprops = {'family':'serif','weight':'bold','size':12 })

#The following groups and counts the amount of patients with each level of bland chromatin. This will be used to make a bar graph. 
df2 = df.groupby(['BlandChromatin'])['BlandChromatin'].count()
print(df2)
#The x_2 variable will create a Numpy array containing each value for bland chromatin, or the x values. 
x_2 = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
#The y_2 variable will create a Numpy array containing the amount of patients with each level of bland chromatin, or the y values. 
y_2 = np.array([150, 159, 161, 39, 34, 9, 71, 28, 11, 20])
#The following sets the bar graph to a specific size using the figure() function. 
plt.figure(figsize = (10, 5))
#This saves the bar plot as a variable so edits (like legends, axis titles, etc.) can be made. The color of the bars on the graph is also determined here. 
bar = plt.bar(x_2,y_2, color = 'orange')
#A call is made to the addlabels fuction, to add labels for each bar. 
addlabels(x_2, y_2)
#This adds a title to the bar graph. 
plt.title('Number of Patients with Each Level of Bland Chromatin', fontdict = title_font)
#This adds a label on the x-axis. 
plt.xlabel('Level of Bland Chromatin', fontdict = small_font)
#This adds a label on the y-axis. 
plt.ylabel('Number of Patients', fontdict = small_font)
#This outputs our desired bar graph. 
plt.show()

