import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
data = pd.read_csv("C:/Users/SHWETA/Pictures/interview documents/creditcard_csv.csv")
print(data)

print(data.head(10))

print(data.tail(10))

print(data.columns)

print(data.describe())

print(data.info())

print(summary(data))

print(data.dtypes)

print(data.Class.unique())

print(data.isnull().sum())

print(data.shape)

print(data['Amount'].value_counts())

print(data['Class'].value_counts())

print(data['Time'].value_counts())

print(data.groupby('Class').agg(['min']))

print(data.groupby('Class').agg(['max']))

print(data.groupby('Amount').agg(['min']))

print(data.groupby('Time').agg(['min']))

print(data.groupby('Time').agg(['max']))

fraud =data.loc[data['Class'] == 1]

normal = data.loc[data['Class'] == 0]
print(fraud.count())

print(len(fraud))
print(len(normal))





