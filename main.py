import matplotlib.pyplot as plt
import pandas as pd
import get_datasets as gd
from reusable_functions import resusable as rf
import numpy as np

filename = 'healthcare-dataset-stroke-data.csv'
location = 'fedesoriano/stroke-prediction-dataset'

gd.get_dataset(filename, location)

# Importing data
df = pd.read_csv(filename, index_col=0)


rf.heatmap_of_missing_values(df)

x = rf.clean_nulls(df)
y = rf.copy_data_set(x)
z = rf.replace_married(y)

m1 = (z.gender == 'Male').sum()
m2 = (z.gender == 'Female').sum()
m3 = (z.gender == 'Other').sum()

m4 = (z.stroke == 1).sum()
m5 = (z.stroke == 0).sum()


labels = 'Male', 'Female', 'Other'
size = [m1,m2, m3]

rf.pie_charts(labels, size)

labels2 = 'Stroke', 'No Stroke'
size2 = [m4, m5]

rf.pie_charts(labels2, size2)

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

labels3 = z.smoking_status.unique()
m10 = pd.DataFrame(z['smoking_status'])
m11 = pd.get_dummies(m10)
size4 = m11.sum()

rf.pie_charts(labels3, size4)


plt.show()