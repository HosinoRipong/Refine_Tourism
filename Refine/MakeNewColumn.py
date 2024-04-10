import pandas as pd

data = pd.read_csv("IntegrateData.csv", encoding='cp949')

# 타겟 변수 설정
target_sex = ['2011_3. 성별', '2013_1.성별', '2015_성별코드', '2017_성별코드', '2019_성별코드', '2021_성별코드', '2023_성별코드'] # 1. 성별
target_age = ['2011_만연령', '2013_2.만나이', '2015_만연령', '2017_만연령', '2019_만연령', '2021_만연령', '2023_만연령'] # 2. 만연령
target_edu = ['2011_6-1. 교육정도', '2013_4.교육정도', '2015_교육정도코드', '2017_교육정도코드', '2019_교육정도코드', '2021_교육정도코드', '2023_교육정도코드'] # 3. 교육정도

# 새로운 데이터프레임 생성
refined_data = pd.DataFrame({})

# 새로운 column 생성
refined_data['sex'] = data[target_sex].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['age'] = data[target_age].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['edu'] = data[target_edu].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

print(refined_data)
refined_data.to_csv('RefinedData.csv', index=False, encoding='cp949') # 데이터 저장 