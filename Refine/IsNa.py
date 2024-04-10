import pandas as pd

data = pd.read_csv("RefinedData.csv", encoding='cp949')

print(data.isna())