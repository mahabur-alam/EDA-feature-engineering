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

# show Cabin column data in view
sns.countplot(data=X_train, x=X_train['Cabin'])
#plt.show()


# Cabin imputer
cabin_imputer = SimpleImputer(missing_values=np.nan, strategy="constant", fill_value="Missing", add_indicator=True)
cabin_imputer.fit(X_train[['Cabin']])

#transform both train and test data
X_train[['Cabin', 'cabin_missing_indicator']]=cabin_imputer.transform(X_train[['Cabin']])
X_test[['Cabin', 'cabin_missing_indicator']]=cabin_imputer.transform(X_test[['Cabin']])

print(X_train)
print(X_test.isnull().sum())