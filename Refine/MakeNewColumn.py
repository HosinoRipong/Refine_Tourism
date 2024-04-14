import pandas as pd

data = pd.read_csv("IntegrateData.csv", encoding='cp949')

# 타겟 변수 설정

## 1. 성별 ~ 5. 전반적인 생활 여건
target_sex = ['2011_3. 성별', '2013_1.성별', '2015_성별코드', '2017_성별코드', '2019_성별코드', '2021_성별코드', '2023_성별코드'] # 1. 성별
target_age = ['2011_만연령', '2013_2.만나이', '2015_만연령', '2017_만연령', '2019_만연령', '2021_만연령', '2023_만연령'] # 2. 만연령
target_education = ['2011_6-1. 교육정도', '2013_4.교육정도', '2015_교육정도코드', '2017_교육정도코드', '2019_교육정도코드', '2021_교육정도코드', '2023_교육정도코드'] # 3. 교육정도
target_satisfied = ['2011_8. 주관적 만족감', '2013_6.주관적만족감', '2015_주관적만족감코드', '2017_주관적만족감코드', '2019_주관적만족감코드', '2021_주관적만족감코드', '2023_주관적만족감코드'] # 4. 주관적만족감
target_life_condition = ['2011_9-1.전반적인 생활여건', '2013_8.생활여건의 변화1-전반적인생활여건', '2015_생활여건변화_전반적생활여건코드', 
                         '2017_생활여건변화_전반적생활여건코드', '2021_생활여건변화_전반적생활여건코드', '2023_생활여건변화_전반적생활여건코드'] # 5. 전반적인 생활 여건

## 6. 생활여건변화_문화여가생활여건 ~ 10. 국내 관광여행 횟수(숙박여행)
target_culture_leisure_condition = ['2011_9-4.문화,여가생활 향유여건', '2013_8.생활여건의 변화4-문화여가생활여건', '2015_생활여건변화_문화여가생활여건코드', '2017_생활여건변화_문화여가생활여건코드', 
                                    '2019_생활여건변화_문화여가생활여건코드', '2021_생활여건변화_문화여가생활여건코드', '2023_생활여건변화_문화여가생활여건코드'] # 6. 생활여건변화_문화여가생활여건
target_is_prepared_old = ['2011_20.본인의 노후 준비방법', '2013_19.노후준비여부', '2015_노후준비방법_본인노후준비여부',
                       '2017_노후준비방법_본인노후준비여부', '2019_노후준비방법_본인노후준비여부', '2021_노후준비방법_본인노후준비여부',
                         '2023_노후준비방법_본인노후준비여부'] # 7. 노후준비여부
target_class_consciousness = ['2011_42-1.계층의식', '2013_40.계층의식', '2015_계층의식코드', '2017_계층의식코드', '2019_계층의식코드', '2021_계층의식코드', '2023_계층의식코드'] # 8. 계층의식
target_class_movement = ['2011_43.계층이동', '2013_41.계층이동', '2015_본인세대_계층이동코드', '2017_본인세대_계층이동코드', '2019_본인세대_계층이동코드', '2021_본인세대_계층이동코드', '2023_본인세대_계층이동코드'] # 9. 계층이동전망
target_count_domestic_lodgment = ['2011_50.숙박여행', '2013_46.숙박여행', '2015_국내관광여행_숙박여행횟수', '2017_국내관광여행_숙박여행횟수',
                                   '2019_국내관광여행_숙박여행횟수', '2021_국내관광여행_숙박여행횟수', '2023_국내관광여행_숙박여행횟수'] # 10. 국내 관광여행 횟수(숙박여행)

## 11. 국내 관광여행 횟수(당일여행) ~ 15. 여가활용 만족도
target_count_domestic_day = ['2011_50.당일여행', '2013_46.당일여행', '2015_국내관광여행_당일여행횟수', '2017_국내관광여행_당일여행횟수',
                              '2019_국내관광여행_당일여행횟수', '2021_국내관광여행_당일여행횟수', '2023_국내관광여행_당일여행횟수'] # 11. 국내 관광여행 횟수(당일여행)
# 12. 국내 관광여행 횟수(합) - 생략
target_count_international = ['2011_51.관광', '2013_47.관광', '2015_해외여행경험_관광횟수', '2017_해외여행경험_관광횟수', '2019_해외여행경험_관광횟수', '2021_해외여행경험_관광횟수', '2023_해외여행경험_관광횟수'] # 13. 해외여행 경험 횟수(관광)
target_with_leisure = ['2011_52-1.여가활동은 누구와 함께?', '2013_48-1.여가활용동반자', '2015_여가활동_동반자코드', '2017_주말여가활동_동반자코드', '2019_주말여가활동_동반자코드', '2021_주말여가활동_동반자코드', '2023_주말여가활동_동반자코드'] # 14. 여가활용동반자
# 15. 여가활용 만족도 - 제거

## 16. 소득 ~ 20. 고용의 안정성
# 16. 소득(주관적) - 제거
# 17. 소득 만족도 - 제거
# 18. 소비생활 만족도 - 제거
target_factor_job = ['2011_61.직업선택요인_1순위', '2013_57.직업선택요인1순위', '2015_직업선택요인_1순위코드', '2017_직업선택요인_1순위코드', '2019_직업선택요인_1순위코드', '2021_직업선택요인_1순위코드', '2023_직업선택요인_1순위코드'] # 19. 직업 선택요인 1순위
target_stability_hire = ['2011_67.고용의 안정성', '2013_63.고용의안정성', '2015_고용안정성코드', '2017_고용안정성코드', '2019_고용안정성코드', '2021_고용안정성코드', '2023_고용안정성코드'] # 20. 고용의 안정성

## 21. 가구소득 ~ 25. 가구주 관계
target_income_household = ['2011_74.가구소득', '2013_73.가구소득', '2015_분류코드_가구소득1코드', '2017_분류코드_가구소득1코드', '2019_분류코드_가구소득1코드', '2021_분류코드_가구소득1코드', '2023_분류코드_가구소득1코드'] # 21. 가구소득
target_number_household = ['2011_가구원수', '2013_분류코드-가구원수', '2015_분류코드_가구원수', '2017_분류코드_가구원수', '2019_분류코드_가구원수', '2021_분류코드_가구원수', '2023_분류코드_가구원수'] # 22. 가구원수
target_city = ['2011_행정구역시도코드', '2013_행정구역시도코드', '2015_행정구역시도코드', '2017_행정구역시도코드', '2019_행정구역시도코드', '2021_행정구역시도코드', '2023_행정구역시도코드'] # 23. 행정구역
target_city_detail = ['2011_동읍면부', '2013_분류코드-동·읍면부', '2015_분류코드_동부읍면부구분코드', '2017_분류코드_동부읍면부구분코드', '2019_분류코드_동부읍면부구분코드', '2021_분류코드_동부읍면부구분코드', '2023_분류코드_동부읍면부구분코드'] # 24. 동읍면부
target_relation_head_household = ['2011_5. 가구주와의 관계', '2013_3.가구주관계', '2015_가구주관계코드', '2017_가구주관계코드', '2019_가구주관계코드', '2021_가구주관계코드', '2023_가구주관계코드'] # 25. 가구주 관계

## 26. 종사상 지위 ~ 30. 일과 가정생활의 우선도
target_status_job = ['2011_70.종사상 지위', '2013_66.종사상지위', '2015_종사상지위코드', '2017_종사상지위코드', '2019_종사상지위코드', '2021_종사상지위코드', '2023_종사상지위코드'] # 26. 종사상 지위
target_status_married = ['2011_7. 혼인상태', '2013_5.혼인상태', '2015_혼인상태코드', '2017_혼인상태코드', '2019_혼인상태코드', '2021_혼인상태코드', '2023_혼인상태코드'] # 27. 혼인상태
target_house_class = ['2011_1. 거처의 종류', '2013_70.거처의종류', '2015_거처종류코드', '2017_거처종류코드', '2019_거처종류코드', '2021_거처종류코드', '2023_거처종류코드'] # 28. 거처 종류
target_house_occupy = ['2011_2. 점유형태', '2013_71.점유형태', '2015_점유형태코드', '2017_점유형태코드', '2019_점유형태코드', '2021_점유형태코드', '2023_점유형태코드'] # 29. 점유 형태
target_priority_work_life = ['2011_66.일과 가정생활의 우선도', '2013_62.일과가정생활의우선', '2015_일가정생활우선도코드', '2017_일가정생활우선도코드', '2019_일가정생활우선도코드', '2021_일가정생활우선도코드', '2023_일가정생활우선도코드'] # 30. 일과 가정생활의 우선도

## 31. 긴축소비지출 1순위 ~ 34. 여행 횟수(합계)
target_austerity_consume = ['2011_58.긴축소비 지출항목_1순위', '2013_54.긴축소비지출항목1순위', '2015_긴축소비지출항목_1순위코드', '2017_긴축소비지출항목_1순위코드', '2019_긴축소비지출항목_1순위코드', '2021_긴축소비지출항목_1순위코드', '2023_긴축소비지출항목_1순위코드'] # 31. 긴축소비지출 1순위
target_is_domestic = ['2011_50.국내 관광여행 횟수', '2013_46.국내여행경험(지난1년간)', '2015_국내관광여행경험여부', '2017_국내관광여행경험여부', '2019_국내관광여행경험여부', '2021_국내관광여행경험여부', '2023_국내관광여행경험여부'] # 32. 국내여행여부
target_is_international = ['2011_51.지난1년간 해외 경험여부', '2013_47.해외여행경험(지난1년간)', '2015_해외여행경험여부', '2017_해외여행경험여부', '2019_해외여행경험여부', '2021_해외여행경험여부', '2023_해외여행경험여부'] # 33. 해외여행여부
# 34. 여행 횟수(합계) - 생략

# 새로운 데이터프레임 생성
refined_data = pd.DataFrame({})

# 새로운 column 생성

## 1. 성별 ~ 5. 전반적인 생활 여건
refined_data['sex'] = data[target_sex].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['age'] = data[target_age].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['education'] = data[target_education].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfied'] = data[target_satisfied].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['life_condition'] = data[target_life_condition].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 6. 생활여건변화_문화여가생활여건 ~ 10. 국내 관광여행 횟수(숙박여행)
refined_data['culture_leisure_condition'] = data[target_culture_leisure_condition].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['is_prepared_old'] = data[target_is_prepared_old].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['class_consciousness'] = data[target_class_consciousness].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['class_movement'] = data[target_class_movement].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['count_domestic_lodgment'] = data[target_count_domestic_lodgment].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 11. 국내 관광여행 횟수(당일여행) ~ 15. 여가활용 만족도
refined_data['count_domestic_day'] = data[target_count_domestic_day].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 12
refined_data['count_international'] = data[target_count_international].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['with_leisure'] = data[target_with_leisure].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 15

## 16. 소득(주관적) ~ 20. 고용의 안정성
# 16
# 17
# 18
refined_data['factor_job'] = data[target_factor_job].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['stability_hire'] = data[target_stability_hire].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 21. 가구소득 ~ 25. 가구주 관계
refined_data['income_household'] = data[target_income_household].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['number_household'] = data[target_number_household].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['city'] = data[target_city].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['city_detail'] = data[target_city_detail].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['relation_head_household'] = data[target_relation_head_household].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 26. 종사상 지위 ~ 30. 일과 가정생활의 우선도
refined_data['status_job'] = data[target_status_job].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['status_married'] = data[target_status_married].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['house_class'] = data[target_house_class].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['house_occupy'] = data[target_house_occupy].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['priority_work_life'] = data[target_priority_work_life].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 31. 긴축소비지출 1순위 ~ 34. 여행 횟수(합계)
refined_data['austerity_consume'] = data[target_austerity_consume].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['is_domestic'] = data[target_is_domestic].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['is_international'] = data[target_is_international].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 34

print(refined_data)
refined_data.to_csv('RefinedData.csv', index=False, encoding='cp949') # 데이터 저장 