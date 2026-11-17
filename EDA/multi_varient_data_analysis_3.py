import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')
print(df.columns)

# show passenger class wise survival chart
'''
sns.barplot(x=df['Pclass'], y=df['Fare'])
plt.show()
'''

sns.barplot(x=df['Survived'], y=df['Age'], hue=df['Sex'])
plt.show()
