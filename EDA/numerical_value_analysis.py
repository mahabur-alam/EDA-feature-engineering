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

# age column histogram plot
sns.histplot(df['Age'], bins=30)
plt.title("Age in Histogram ")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
