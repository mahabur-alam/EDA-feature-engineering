import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')

# 1. Display the dataset information, including column names, data types, and non-null values.
print(df.info())

# 2. Generate a statistical summary of the numerical columns.
print(df.describe())


# 3. Identify which columns contain numerical data and which contain non-numerical data.
print(df.dtypes)

print("Numerical Columns:")
print(df.select_dtypes(include='number').columns.tolist())

print("\nNon-Numerical Columns:")
print(df.select_dtypes(exclude='number').columns.tolist())