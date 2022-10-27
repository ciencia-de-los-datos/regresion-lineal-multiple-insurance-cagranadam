import pandas as pd

df = pd.read_csv("insurance.csv", sep= ",")

    # Asigne la columna `charges` a la variable `y`.
y = df["charges"]

    # Asigne una copia del dataframe `df` a la variable `X`.
X = df.copy()

    # Remueva la columna `charges` del DataFrame `X`.
X= X.drop("charges", axis=1)


p= 1- ((1339 - 300)/1339)
print(p)