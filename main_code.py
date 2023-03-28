import pandas as pd
import numpy as nm

df = pd.read_csv('onlineRetail.csv', sep = ',', encoding='utf-8', encoding_errors='ignore')

df.dropna(inplace = True)

#print(df.head(10))
print(df.to_string())