import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
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
#print(df.to_string())

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
#This outputs our desired graphs. 
plt.show()

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
bar = plt.bar(x_2,y_2, color = 'mediumturquoise')
#A call is made to the addlabels fuction, to add labels for each bar. 
addlabels(x_2, y_2)
#This adds a title to the bar graph. 
plt.title('Number of Patients with Each Level of Bland Chromatin', fontdict = title_font)
#This adds a label on the x-axis. 
plt.xlabel('Level of Bland Chromatin', fontdict = small_font)
#This adds a label on the y-axis. 
plt.ylabel('Number of Patients', fontdict = small_font)
#This outputs our desired graphs. 
plt.show()

#This takes the data from the ClumpThick, UnifCellSize, and UnifCellShape column of our dataframe and creates a histogram out of it. It will show the frequency of each value from 1-10 in each column. 
x_3 = list(df['ClumpThick'])
x_4 = list(df['UnifCellSize'])
x_5 = list(df['UnifCellShape'])
#This will assign colors and labels for each column. 
colors = ['lightcoral', 'sandybrown', 'khaki']
labels = ['Clump Thickness', 'Uniform Cell Size', 'Uniform Cell Shape']
plt.figure(figsize = (10,5))
#This saves the plot as a hist variable so it can be adjusted or used later. 
hist = plt.hist([x_3, x_4, x_5], color = colors, label = labels, bins = 10)
#This adds a legend to our graph. 
plt.legend()
#This adds a title to our graph, with the matching title font from before. 
plt.title('Histogram of Multiple Breast Cancer Attributes', fontdict = title_font)
#This adds a x-axis label to the graph, with the matching small font from before. 
plt.xlabel('Degree of Each Category', fontdict = small_font)
#This adds a y-axis label to the graph, with the matching small font from before. 
plt.ylabel('Number of Patients', fontdict = small_font)
#This outputs our desired graphs. 
plt.show()

#The following saves columns that will be used to compare datapoints on a scatterplot. 
x_6 = df['UnifCellSize'].to_numpy()
y_3 = df['UnifCellShape'].to_numpy()
#The following sets the bar graph to a specific size using the figure() function. 
plt.figure(figsize = (10, 5))
#This adds a title to our graph, with the matching title font from before. 
plt.title('Scatterplot of Uniformity of Cell Shape and Size', fontdict = title_font)
#This adds a x-axis label to the graph, with the matching small font from before. 
plt.xlabel('Uniformity of Cell Shape', fontdict = small_font)
#This adds a y-axis label to the graph, with the matching small font from before. 
plt.ylabel('Uniformity of Cell Size', fontdict = small_font)
#This plots the points using each column as an x and y. The scatter plot will be used to see if there is a relationship. 
colors = np.arange(0,682)
plt.scatter(x_6, y_3, c=colors, cmap='viridis')
#This prints the colorbar that shows the range of values. 
plt.colorbar()
#This outputs our desired graphs.
plt.show()

#Here pandas sample() function is used to split the data randomly into a training data set and a testing, or verification set. 
#This takes a percentage of the data points randomly and saves them as a copy of the original data frame. 
training_data = df.sample(frac=0.8, random_state=25)
#This code just removes the data already in the training, data based on the indexes, from a copy of the original dataframe. 
testing_data = df.drop(training_data.index)
#The following prints out the amount of data points in each example. 
print(f"Size of Training Set: {training_data.shape[0]}")
print(f"Size of Validation Set: {testing_data.shape[0]}")

#Here, scikit train_test_split splits the data and returns a list which contains two NumPy arrays, while train_size = .75 puts 75 percent of the data into a training set and the remaining 25 percent into a testing set.
training_data2, testing_data2 = train_test_split(df, random_state=0, train_size = .75)
#The following prints out the amount of data points in each example. 
print(f"Size of Training Set: {training_data2.shape[0]}")
print(f"Size of Validation Set: {testing_data2.shape[0]}")
