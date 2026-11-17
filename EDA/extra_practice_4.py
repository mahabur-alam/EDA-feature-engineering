import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/titanic_data_updated.csv')

# 1. Count the total number of duplicate rows.
print(f"total number of duplicate rows: \n{df.duplicated().sum()}\n")


# 2. Create a separate DataFrame without duplicate rows.
copy_dataframe = df.copy()
without_duplicate_rows = copy_dataframe.drop_duplicates()
print(without_duplicate_rows)