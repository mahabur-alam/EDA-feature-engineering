import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')
print(df.columns)

# showing Passenger Class wise Survived chat
sns.countplot(x=df['Pclass'], hue=df['Survived'])
#plt.show()

# showing Passenger Class wise Survived count and ratio
pclass_split = df.groupby('Pclass')['Survived'].value_counts()
print(pclass_split)

pclass_survived_ratio = df.groupby('Pclass')['Survived'].value_counts(normalize=True)
print(pclass_survived_ratio)
