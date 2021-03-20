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


# Function to check for nulls and replace with 0
def clean_nulls(data):
    bool_series = data.isnull().sum()
    x = bool_series[bool_series > 0]
    if len(x) > 0:
        data.fillna(0, inplace=True)
        return data
    else:
        return


# creating a copy of original dataset for treating missing values
def copy_data_set(data2):
    st_copy = data2.copy(deep=True)
    return st_copy

# Replace Married Values with numeric
def replace_married(data3):
    data3['ever_married'] = data3['ever_married'].replace({'Yes': 1, 'No': 0})
    return data3


x = clean_nulls(df)
y = copy_data_set(x)
z = replace_married(y)


df_split = z[['work_type', 'Residence_type', 'smoking_status', 'gender']]

df_split2 =z[['age', 'ever_married', 'avg_glucose_level', 'bmi', 'stroke']]

print(df_split.head())
print(df_split2.head())


abc = pd.get_dummies(df_split, drop_first=True)

abc = pd.merge(df_split2, abc, left_index=True, right_index=True)

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


#st_copy=pd.get_dummies(st_copy,drop_first=True)
