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

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from feature_target_column import X_train, X_test, y_train, y_test, df


# show embarked column data in view
sns.countplot(data=df, x=df['Embarked'])
plt.show()

# Embarked imputer
embarked_imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
embarked_imputer.fit(X_train[['Embarked']])

#transform both train and test data
X_train['Embarked']=embarked_imputer.transform(X_train[['Embarked']]).ravel() # convert 2D to 1D
X_test['Embarked']=embarked_imputer.transform(X_test[['Embarked']]).ravel() # convert 2D to 1D

print(X_train.isnull().sum())