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

# survived column count plot
'''sns.countplot(data=df, x=df['Survived'])
plt.show()'''

# survived columns count & %
print(df['Survived'].value_counts())
print(df['Survived'].value_counts()/ len(df) * 100)

survived = df['Survived'].value_counts()
survived_category = df['Survived'].unique()

plt.title("Showing survived ration using pie chart")
plt.pie(survived, labels=survived_category, autopct='%1.1f')
plt.show()