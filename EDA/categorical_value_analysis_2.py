'''
univariate analysis:
1. categorical data
2. numerical data
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load data
df = pd.read_csv('../datasets/titanic_data_updated.csv')
print(df.columns)

# pclass
sns.countplot(data=df, x='Pclass')
plt.show()

# Pclass count
print(df['Pclass'].value_counts())

# Pclass count %
print(df['Pclass'].value_counts() / len(df) * 100)


# show in pie chart
passenger_class_count = df['Pclass'].value_counts()
passenger_class = df['Pclass'].unique()

plt.title("showing passenger class ratio using pie chart")
plt.pie(passenger_class_count, labels=passenger_class, autopct='%1.1f')
plt.show()
