import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')
# 1. Display the first 10 rows of the dataset.
print(df.head(10))

# 2. Display 10 random rows.
print(df.sample(10))

# 3. Find the total number of rows and columns.
print(f"Showing number of Rows & Columns: {df.shape}")

# 4. Print the number of rows and the number of columns separately.
print(f"number of rows: {df.shape[0]}")
print(f"number of columns: {df.shape[1]}")