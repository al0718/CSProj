import pandas as pd
import numpy as nm
#Reads the csv with proper encoding. 
df = pd.read_csv('onlineRetailGITHUB.csv', sep = ',', encoding='utf-8', encoding_errors='ignore')
#Deletes rows in the original DataFrame with missing cells. 
df.dropna(inplace = True)
#Turns InvoiceNo column to a float column. 
df['InvoiceNo'] = df['InvoiceNo'].str.replace('\D', '', regex=True)
df['InvoiceNo'] = df['InvoiceNo'].astype(float)
#Calculates the mean, median, variance, and standard deviation of the UnitPrice and InvoiceNo columns. 
priceMean = df["UnitPrice"].mean()
invoiceMean = df["InvoiceNo"].mean()
priceMed = df["UnitPrice"].median()


print(df.head(10))
#print(df.to_string())

print(priceMean)
print(int(invoiceMean))
print(priceMed)
