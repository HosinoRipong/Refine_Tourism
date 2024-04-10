import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data2011 = pd.read_csv('tour2011.csv', encoding='cp949')
data2013 = pd.read_csv('tour2013.csv', encoding='cp949')
data2015 = pd.read_csv('tour2015.csv', encoding='cp949')
data2017 = pd.read_csv('tour2017.csv', encoding='cp949')
data2019 = pd.read_csv('tour2019.csv', encoding='cp949')
data2021 = pd.read_csv('tour2021.csv', encoding='cp949')
data2023 = pd.read_csv('tour2023.csv', encoding='cp949')

for old_column in data2011.columns:
    new_column = f"2011_{old_column}"  # 새로운 열 이름 생성
    data2011.rename(columns={old_column: new_column}, inplace=True)  # 열 이름 변경

for old_column in data2013.columns:
    new_column = f"2013_{old_column}"  # 새로운 열 이름 생성
    data2013.rename(columns={old_column: new_column}, inplace=True)  # 열 이름 변경

for old_column in data2015.columns:
    new_column = f"2015_{old_column}"  # 새로운 열 이름 생성
    data2015.rename(columns={old_column: new_column}, inplace=True)  # 열 이름 변경

for old_column in data2017.columns:
    new_column = f"2017_{old_column}"  # 새로운 열 이름 생성
    data2017.rename(columns={old_column: new_column}, inplace=True)  # 열 이름 변경

for old_column in data2019.columns:
    new_column = f"2019_{old_column}"  # 새로운 열 이름 생성
    data2019.rename(columns={old_column: new_column}, inplace=True)  # 열 이름 변경

for old_column in data2021.columns:
    new_column = f"2021_{old_column}"  # 새로운 열 이름 생성
    data2021.rename(columns={old_column: new_column}, inplace=True)  # 열 이름 변경

for old_column in data2023.columns:
    new_column = f"2023_{old_column}"  # 새로운 열 이름 생성
    data2023.rename(columns={old_column: new_column}, inplace=True)  # 열 이름 변경


merged_data = pd.concat([data2011, data2013], axis=0, ignore_index=True)
merged_data = pd.concat([merged_data, data2015], axis=0, ignore_index=True)
merged_data = pd.concat([merged_data, data2017], axis=0, ignore_index=True)
merged_data = pd.concat([merged_data, data2019], axis=0, ignore_index=True)
merged_data = pd.concat([merged_data, data2021], axis=0, ignore_index=True)
merged_data = pd.concat([merged_data, data2023], axis=0, ignore_index=True)


print(merged_data)
merged_data.to_csv('IntegrateData.csv', index=False, encoding='cp949')  # index=False를 지정하면 인덱스를 파일에 저장하지 않습니다.
