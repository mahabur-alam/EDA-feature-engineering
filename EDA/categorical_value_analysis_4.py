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

# Embarked cloumn
sns.countplot(data=df, x='Embarked')
plt.show()

# Embarked count & count %
print(df['Embarked'].value_counts())
print(df['Embarked'].value_counts() / len(df) * 100)


# pie chart in Embarked
total_Embarked = df['Embarked'].value_counts()
unique_Embarked = df['Embarked'].unique()
print(unique_Embarked)

plt.pie(total_Embarked, labels=unique_Embarked, autopct='%1.1f')
plt.show()
