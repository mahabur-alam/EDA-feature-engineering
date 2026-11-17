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

# show data type of this dataset at a glance
print(df.info())

# plot on Fare column
sns.histplot(df['Fare'], bins=50)

plt.title('Histogram of Fare Column')
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()


# KDE Plot
sns.kdeplot(df['Fare'])

plt.title('KDE plot of Fare')
plt.xlabel('Fare')
plt.ylabel('Probability Distribution')
plt.show()

# box plot
sns.boxplot(df['Fare'])

plt.show()