import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
print(df)

#scatter plot
sns.scatterplot(data=df,
                x=df['total_bill'],
                y=df['tip'],
                hue=df['sex'],
                size=df['size']
                )
plt.show()
