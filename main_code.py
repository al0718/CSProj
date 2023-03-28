import pandas as pd
import numpy as nm
#Reads the csv with proper encoding. 
df = pd.read_csv('onlineRetailGITHUB.csv', sep = ',', encoding='utf-8', encoding_errors='ignore')
#Deletes rows in the original DataFrame with missing cells. 
df.dropna(inplace = True)
#Turns InvoiceNo column to a float column. 
df['InvoiceNo'] = df['InvoiceNo'].str.replace('\D', '', regex=True)
df['InvoiceNo'] = df['InvoiceNo'].astype(float)
df['UnitPrice'] = df['UnitPrice'].astype(float)
#Calculates the mean, median, mode, variance, and standard deviation of the UnitPrice and InvoiceNo columns. 
priceMean = df["UnitPrice"].mean()
invoiceMean = df["InvoiceNo"].mean()
priceMed = df["UnitPrice"].median()
invoiceMed = df["InvoiceNo"].mean()
priceMode = df["UnitPrice"].mode()
invoiceMode = df["InvoiceNo"].mode()
priceVar = df["UnitPrice"].var()
invoiceVar = df["InvoiceNo"].var()
priceStand = df["UnitPrice"].std()
invoiceStand = df["InvoiceNo"].std()

#print(df.head(10))
#print(df.to_string())

print(priceMean)
print(int(invoiceMean))
print(priceMed)
print(int(invoiceMed))
print(priceMode)
print(int(invoiceMode))
print(priceVar)
print(invoiceVar)
print(priceStand)
print(invoiceStand)
