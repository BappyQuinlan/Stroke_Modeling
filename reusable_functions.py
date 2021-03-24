# Reusable Functions
# Author : Barry Quinlan
# Date : 24th March 2021
# Email : bappyquinlan@gmail.com

import matplotlib.pyplot as plt
import seaborn as sns

class resusable:

    #Generate Heatmap
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

    # Generate Pie Charts
    def pie_charts(labels, axis):
        fig1, ax1 = plt.subplots(figsize=[10, 8])
        ax1.pie(axis, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.legend()
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        return
