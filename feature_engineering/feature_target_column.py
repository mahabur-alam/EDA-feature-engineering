import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('../datasets/titanic_data_updated.csv')
#print(df)

# drop un-necessary column
df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
#print(df.head())

# feature column
X = df.drop(['Survived'], axis=1)
#print(X.head())

# Target column
y = df['Survived']
#print(y.head())

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train)
