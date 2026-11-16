import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load data
df = pd.read_csv('../datasets/titanic_data_updated.csv')
# show only 1st 10 data
#print(df.head(10))

#show random 10 data
rand_data  = df.sample(10)
#print(rand_data)

# data set columns
dataset_columns = df.shape
print(dataset_columns)

# show null columns data
# isnull() shows all columns wise row data & isnull().sum() shows columns wise row summary data
#print(f"Null Values of total dataset: \n{df.isnull().sum()}")

# show duplicate data
#print(f"Duplicate Data: {df.duplicated().sum()}")

# data statistical information
#print(df.describe())

# dataset data type and show null data
print(df.info())
