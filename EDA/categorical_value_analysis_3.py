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

# Sex cloumn
sns.countplot(data=df, x='Sex')
plt.show()

# sex count & count %
print(df['Sex'].value_counts())
print(df['Sex'].value_counts() / len(df) * 100)


# pie chart in sex
total_sex = df['Sex'].value_counts()
unique_sex = df['Sex'].unique()

plt.pie(total_sex, labels=unique_sex, autopct='%1.1f')
plt.show()
