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
df = pd.read_csv(filename)

# Function to check for nulls and replace with 0
def clean_nulls(data):
    bool_series = data.isnull().sum()
    x = bool_series[bool_series > 0]
    if len(x) > 0:
        data.fillna(0, inplace=True)
        return data
    else:
        return

# # creating a copy of original dataset for treating missing values
# st_copy = df.copy(deep=True)
# st_copy['ever_married'] = st_copy['ever_married'].replace({'Yes': 1, 'No': 0})
# st_copy['bmi'].fillna(0)
# st_copy2 = pd.DataFrame(st_copy, columns=['id','work_type'])
# st_copy2.set_index('id', inplace=True)


print(clean_nulls(df))

