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

data.to_csv('RefinedData.csv', index=False, encoding='cp949') # 데이터 저장 