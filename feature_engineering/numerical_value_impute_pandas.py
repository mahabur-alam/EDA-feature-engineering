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

from feature_target_column import X_train, X_test, y_train, y_test
import seaborn as sns
import matplotlib.pyplot as plt

#print("Missing values in X_train:")
#print(f"Missing values in X train{X_train.isnull().sum()}\n")

#print(f"\nMissing values in X Test: {X_test.isnull().sum()}")


# mean imputer
age_mean = X_train['Age'].mean()
#print(age_mean)

X_train['age_mean_imputor'] = X_train['Age'].fillna(age_mean)
#print(X_train)
#print(X_train.isnull().sum())
X_test['age_mean_imputor'] = X_test['Age'].fillna(age_mean)
#print(X_test.isnull().sum())

# median imputer
age_median = X_train['Age'].median()
#print(age_median)

X_train['age_median_imputor'] = X_train['Age'].fillna(age_median)
#print(X_train)
#print(X_train.isnull().sum())
X_test['age_median_imputor'] = X_test['Age'].fillna(age_median)
#print(X_test.isnull().sum())


# KDE plot
sns.kdeplot(data=X_train, x='age_mean_imputor')
plt.show()

sns.kdeplot(data=X_train, x='age_median_imputor')
plt.show()