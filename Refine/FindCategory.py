import pandas as pd

data = pd.read_csv("IntegrateData.csv", encoding='cp949')

# 여러 검색어
search_words = ['대분류']

# 검색어가 포함된 열 이름 찾기
found_columns = {}
for word in search_words:
    found_columns[word] = [col for col in data.columns if word in col]

# 찾은 열 이름 출력
for category, columns in found_columns.items():
    print(f"{category} : {', '.join(columns)}")