import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')
print(df.columns)

# show passenger age wise survival chart using KDE plot
sns.kdeplot(data=df, x=df['Age'], hue=df['Survived'])
plt.show()
