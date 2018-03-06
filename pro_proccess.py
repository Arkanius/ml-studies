import pandas as pd 
data = pd.read_csv('credit-data.csv')
data.describe()

data.loc[data['age'] < 0] #busca no array todos os valores da colune age que sejam menores do que 0

data.drop(data[data.age < 0].index, inplace=True)


data['age'][data.age > 0].mean()

data.loc[data['age'] < 0]

pd.isnull(data['age'])

data.loc[pd.isnull(data['age'])]

prev = data.iloc[:, 1:4].values
nclass = data.iloc[:, 4].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(prev[:, 0:3])
prev[:, 0:3] = imputer.transform(prev[:, 0:3])

print(prev)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(prev)