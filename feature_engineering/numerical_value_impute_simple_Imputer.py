'''
2 way we can impute numerical missing values:
    1. mean value
    2. median value
'''

'''
fill missing value using:
    1. pandas -> fillna()
    2. ML -> eco system (sk learn) : simple imputer()
'''
import numpy as np
from sklearn.impute import SimpleImputer
from feature_target_column import X_train, X_test, y_train, y_test
import seaborn as sns
import matplotlib.pyplot as plt

'''
    1. fit - learn
    2. transform - fill up 
'''
age_imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
age_imputer.fit(X_train[['Age']]) # fit get 2d data

X_train['Age'] = age_imputer.transform(X_train[['Age']]).ravel()
X_test['Age'] = age_imputer.transform(X_test[['Age']]).ravel()

print(X_train.isnull().sum())
print(X_test)