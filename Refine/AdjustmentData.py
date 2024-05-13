import pandas as pd
import numpy as np

data = pd.read_csv("RefinedData.csv", encoding='cp949')

# 조정 0 : 10. 국내 관광여행 횟수(숙박여행), 11. 국내 관광여행 횟수(당일여행), 13. 해외여행 경험 횟수(관광)
data['count_domestic_lodgment'] = data['count_domestic_lodgment'].fillna(0)
data['count_domestic_day'] = data['count_domestic_day'].fillna(0)
data['count_international'] = data['count_international'].fillna(0)


# 조정 1 : 8. 계층 의식 - 제거

# 조정 2 : 14. 여가활용동반자 - 제거

# 조정 3 : 19. 직업 선택요인 1순위 - 제거

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

# 조정 8 : 28. 거처 종류 - 제거

# 조정 9 : 31. 긴축소비지출 1순위, 35. 긴축소비지출 2순위, 36. 긴축소비지출 3순위
data.loc[((data['year'] == 2021) | (data['year'] == 2023)) & (data['austerity_consume_first'] == 7), 'austerity_consume_first'] = 11
data.loc[((data['year'] == 2021) | (data['year'] == 2023)) & (data['austerity_consume_second'] == 7), 'austerity_consume_second'] = 11
data.loc[((data['year'] == 2021) | (data['year'] == 2023)) & (data['austerity_consume_third'] == 7), 'austerity_consume_third'] = 11

data.loc[((data['year'] == 2021) | (data['year'] == 2023)) & (data['austerity_consume_first'] >= 8), 'austerity_consume_first'] -= 1
data.loc[((data['year'] == 2021) | (data['year'] == 2023)) & (data['austerity_consume_second'] >= 8), 'austerity_consume_second'] -= 1
data.loc[((data['year'] == 2021) | (data['year'] == 2023)) & (data['austerity_consume_third'] >= 8), 'austerity_consume_third'] -= 1

# 조정 10 : 34. 여행 횟수(합계)
data['count_total'] = data['count_domestic_total'].fillna(0) + data['count_international'].fillna(0)

# 조정 11 : 3. 교육정도
data.loc[data['education'] >= 6, 'education'] = 6

# 조정 12 : 나이 제곱
data['age_square'] = data['age'] ** 2

# 조정 13 : 장애인복지카드 소유여부
data['disabled_welfarecard'] = data['disabled_welfarecard'].replace('W010', 1)
data['disabled_welfarecard'] = data['disabled_welfarecard'].replace('W020', 2)

# 조정 14 : 긴축소비여부에 따른 여행 선호도 평가
data['prefer_tourism'] = 0

data.loc[(data['austerity_consume_first'] != 6) & 
         (data['austerity_consume_second'] != 6) & 
         (data['austerity_consume_third'] != 6), 'prefer_tourism'] = 1

# 조정 15 : 나이대 설정
def categorize_age(age):
    if age < 20:
        return 1
    elif age < 30:
        return 2
    elif age < 40:
        return 3
    elif age < 50:
        return 4
    elif age < 60:
        return 5
    elif age < 70:
        return 6
    else:
        return 7
    
data['age_group'] = data['age'].apply(categorize_age)
 
# 조정 16 : 27. 혼인상태코드
data.loc[(data['year'] == 2017) & (data['status_married'] == 3), 'status_married'] = 1
data.loc[(data['year'] == 2017) & (data['status_married'] > 3), 'status_married'] -= 1

# 조정 17 : 48. 임금근로자
data.loc[data['year'] == 2011, 'satisfy_wage_worker'] = np.nan

# 조정 18 : 49. 산업코드
data['worker_industry'] = data['worker_industry'].replace('A', 1)
data['worker_industry'] = data['worker_industry'].replace('B', 2)
data['worker_industry'] = data['worker_industry'].replace('C', 3)
data['worker_industry'] = data['worker_industry'].replace('D', 4)
data['worker_industry'] = data['worker_industry'].replace('E', 5)
data['worker_industry'] = data['worker_industry'].replace('F', 6)
data['worker_industry'] = data['worker_industry'].replace('G', 7)
data['worker_industry'] = data['worker_industry'].replace('H', 8)
data['worker_industry'] = data['worker_industry'].replace('I', 9)
data['worker_industry'] = data['worker_industry'].replace('J', 10)
data['worker_industry'] = data['worker_industry'].replace('K', 11)
data['worker_industry'] = data['worker_industry'].replace('L', 12)
data['worker_industry'] = data['worker_industry'].replace('M', 13)
data['worker_industry'] = data['worker_industry'].replace('N', 14)
data['worker_industry'] = data['worker_industry'].replace('O', 15)
data['worker_industry'] = data['worker_industry'].replace('P', 16)
data['worker_industry'] = data['worker_industry'].replace('Q', 17)
data['worker_industry'] = data['worker_industry'].replace('R', 18)
data['worker_industry'] = data['worker_industry'].replace('S', 19)
data['worker_industry'] = data['worker_industry'].replace('T', 20)
data['worker_industry'] = data['worker_industry'].replace('U', 21)

data['worker_industry'] = data['worker_industry'].replace('a', 1)
data['worker_industry'] = data['worker_industry'].replace('b', 2)
data['worker_industry'] = data['worker_industry'].replace('c', 3)
data['worker_industry'] = data['worker_industry'].replace('d', 4)
data['worker_industry'] = data['worker_industry'].replace('e', 5)
data['worker_industry'] = data['worker_industry'].replace('f', 6)
data['worker_industry'] = data['worker_industry'].replace('g', 7)
data['worker_industry'] = data['worker_industry'].replace('h', 8)
data['worker_industry'] = data['worker_industry'].replace('i', 9)
data['worker_industry'] = data['worker_industry'].replace('j', 10)
data['worker_industry'] = data['worker_industry'].replace('k', 11)
data['worker_industry'] = data['worker_industry'].replace('l', 12)
data['worker_industry'] = data['worker_industry'].replace('m', 13)
data['worker_industry'] = data['worker_industry'].replace('n', 14)
data['worker_industry'] = data['worker_industry'].replace('o', 15)
data['worker_industry'] = data['worker_industry'].replace('p', 16)
data['worker_industry'] = data['worker_industry'].replace('q', 17)
data['worker_industry'] = data['worker_industry'].replace('r', 18)
data['worker_industry'] = data['worker_industry'].replace('s', 19)
data['worker_industry'] = data['worker_industry'].replace('t', 20)
data['worker_industry'] = data['worker_industry'].replace('u', 21)

# 조정 19 : 50. 직업코드
data['worker_job'] = data['worker_job'].replace('A', 10)

# 조정 20 : 51. 국내숙박여행 유무
data['is_domestic_lodgment'] = 0
data.loc[(data['count_domestic_lodgment'] > 0 ), 'is_domestic_lodgment'] = 1
data.loc[(data['count_domestic_lodgment'] == 0 ), 'is_domestic_lodgment'] = 2
data.loc[(data['is_domestic_lodgment'] == 0 ), 'is_domestic_lodgment'] = np.nan

# 조정 21 : 52. 국내당일치기여행 유무
data['is_domestic_day'] = 0
data.loc[(data['count_domestic_day'] > 0 ), 'is_domestic_day'] = 1
data.loc[(data['count_domestic_day'] == 0 ), 'is_domestic_day'] = 2
data.loc[(data['is_domestic_day'] == 0 ), 'is_domestic_day'] = np.nan


# 조정 : 임금근로자만 따로 데이터프레임 생성
data = data[data['status_job'] == 4]

# data.to_csv('RefinedData.csv', index=False, encoding='cp949') # 데이터 저장
data.to_csv('RefinedData_unpaid_family.csv', index=False, encoding='cp949') # 데이터 저장