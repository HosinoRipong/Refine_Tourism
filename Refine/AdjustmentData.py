import pandas as pd

data = pd.read_csv("RefinedData.csv", encoding='cp949')

# 조정 1 : 8. 계층 의식
data['class_consciousness'] = data['class_consciousness'] % 10

# 조정 2 : 14. 여가활용동반자
data['with_leisure'] = data['with_leisure'].replace(6, 5)

# 조정 3 : 19. 직업 선택요인 1순위
data['factor_job'] = data['factor_job'].replace(9, 8)

# 조정 4 : 12. 국내 관광여행 횟수(합) 추가
data['count_domestic_total'] = data['count_domestic_lodgment'].fillna(0) + data['count_domestic_day'].fillna(0)

# 조정 5 : 21. 가구소득
data['income_household'] = data['income_household'].replace(8, 7)
for index, value in data['income_household'].items():
    if value > 100:
        data.at[index, 'income_household'] = (value % 100) / 10
data['income_household'] = data['income_household'].replace(7.8, 7)

# 조정 6 : 22. 가구원수
data['number_household'] = data['number_household'] % 10

# 조정 7 : 24. 동읍면부
data['city_detail'] = data['city_detail'].replace('00A', 1)
data['city_detail'] = data['city_detail'].replace('00B', 2)
data['city_detail'] = data['city_detail'].replace(3, 1)
data['city_detail'] = data['city_detail'].replace(4, 2)

# 조정 8 : 28. 거처 종류
data['house_class'] = data['house_class'].replace(5, 4)

# 조정 9 : 31. 긴축소비지출 1순위
# 조정 필요

# 조정 10 : 34. 여행 횟수(합계)
data['count_total'] = data['count_domestic_total'].fillna(0) + data['count_international'].fillna(0)

data.to_csv('RefinedData.csv', index=False, encoding='cp949') # 데이터 저장 