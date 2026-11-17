import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')

# 1. Count the missing values in each column.
print(f"missing values in each column: \n{df.isnull().sum()}\n")

# 2. Display only the columns that contain missing values.
missing = df.isnull().sum()
print(f"only the columns that contain missing values: \n{missing[missing > 0]}\n")

# 3. Identify the column with the highest number of missing values.
missing_counts = df.isnull().sum()
max_missing_column = missing_counts.idxmax()
max_missing_value = missing_counts.max()
print(f"column with the highest number of missing values: \n{max_missing_column}: {max_missing_value}")


