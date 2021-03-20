import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import get_datasets as gd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

filename = 'healthcare-dataset-stroke-data.csv'
location = 'fedesoriano/stroke-prediction-dataset'

gd.get_dataset(filename, location)

# Importing data
df = pd.read_csv(filename, index_col=0)

#y = pd.get_dummies(df, drop_first=True)

#print(df.head())

df_split = df[['gender']]

df_split2 =df[['age', 'ever_married', 'avg_glucose_level', 'bmi', 'stroke']]


df_split['Male'] = 0
df_split['Female'] = 0
df_split.loc[df_split['gender'] == 'Male', 'Male'] = 1
df_split.loc[df_split['gender'] == 'Female', 'Female'] = 1


labels = 'Male', 'Female'
size1 = [df_split['Male'].sum(), df_split['Female'].sum()]

fig1, ax1 = plt.subplots()
ax1.pie(size1, labels=labels, autopct='%1.1f%%',
         shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()