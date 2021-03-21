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


def heatmap_of_missing_values(data):
    plt.title('Missing Value Status', fontweight='bold')
    ax = sns.heatmap(data.isna().sum().to_frame(), annot=True, fmt='d', cmap='vlag')
    ax.set_xlabel('Amount Missing')
    return


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


def pie_charts(labels, axis):
    fig1, ax1 = plt.subplots()
    ax1.pie(axis, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    return


fig1 = heatmap_of_missing_values(df)

x = clean_nulls(df)
y = copy_data_set(x)
z = replace_married(y)

m1 = (z.gender == 'Male').sum()
m2 = (z.gender == 'Female').sum()
m3 = (z.gender == 'Other').sum()

m4 = (z.stroke == 1).sum()
m5 = (z.stroke == 0).sum()


labels = 'Male', 'Female', 'Other'
size = [m1,m2, m3]

pie_chart1 = pie_charts(labels, size)


labels2 = 'Stroke', 'No Stroke'
size2 = [m4, m5]

list_of_tuples = list(zip(df.query('gender=="Female"').age, df.query('gender=="Male"').age))
list_of_tuples
dist = pd.DataFrame(list_of_tuples,columns=['female', 'male'])
dist = dist.astype(int)

plt.figure(figsize=[10,8])
x = dist['female']
y = dist['male']

plt.hist([x,y],color=['cyan', 'magenta'], label=['female', 'male'])
plt.title('Male V Female Ages')
plt.grid()
plt.legend()
plt.xlabel('Ages')
plt.ylabel('Count')

#pie_chart2 = pie_charts(pd.DataFrame)


plt.show()