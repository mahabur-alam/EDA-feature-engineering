# import the feature_target_column.py file as a module
# this gives access to its train/test split (X_train, X_test, y_train, y_test)
#from feature_target_column import X_train, X_test, y_train, y_test

# check missing values in the training features
#print("Missing values in X_train:")
#print(X_train.isnull().sum())


import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('../datasets/titanic_data_updated.csv')

# finding missing values
missing_value = df.isnull().sum()
print(missing_value)