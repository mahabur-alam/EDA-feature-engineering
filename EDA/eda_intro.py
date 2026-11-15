import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
df = pd.read_csv('../datasets/titanic_data_updated.csv')
# show only 1st 10 data
#print(df.head(10))
#show random 2 data
old_data  = df.sample(10)
!print(old_data)

# data set column
columns = df.shape()
print(columns)
