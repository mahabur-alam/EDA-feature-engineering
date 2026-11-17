import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')
#print(df)

# show sex wise survival chart
sns.countplot(x=df['Sex'], hue=df['Survived'])
#plt.show()

# now showing sex wise survival count and ratio
gender_split = df.groupby('Sex')['Survived'].value_counts()
print(gender_split)

gernder_split_ratio = df.groupby('Sex')['Survived'].value_counts(normalize=True)
print(gernder_split_ratio)
