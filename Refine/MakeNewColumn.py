import pandas as pd

data = pd.read_csv("IntegrateData.csv", encoding='cp949')

# 타겟 변수 설정

# 0. 연도
target_year = ['2011_Year','2013_Year','2015_Year','2017_Year','2019_Year','2021_Year','2023_Year']

## 1. 성별 ~ 5. 전반적인 생활 여건
target_sex = ['2011_3. 성별', '2013_1.성별', '2015_성별코드', '2017_성별코드', '2019_성별코드', '2021_성별코드', '2023_성별코드'] # 1. 성별
target_age = ['2011_만연령', '2013_2.만나이', '2015_만연령', '2017_만연령', '2019_만연령', '2021_만연령', '2023_만연령'] # 2. 만연령
target_education = ['2011_6-1. 교육정도', '2013_4.교육정도', '2015_교육정도코드', '2017_교육정도코드', '2019_교육정도코드', '2021_교육정도코드', '2023_교육정도코드'] # 3. 교육정도
# 4. 주관적만족감 - 제거
# 5. 전반적인 생활 여건 - 제거

## 6. 생활여건변화_문화여가생활여건 ~ 10. 국내 관광여행 횟수(숙박여행)
# 6. 생활여건변화_문화여가생활여건 - 제거
target_is_prepared_old = ['2011_20.본인의 노후 준비방법', '2013_19.노후준비여부', '2015_노후준비방법_본인노후준비여부',
                       '2017_노후준비방법_본인노후준비여부', '2019_노후준비방법_본인노후준비여부', '2021_노후준비방법_본인노후준비여부',
                         '2023_노후준비방법_본인노후준비여부'] # 7. 노후준비여부
# 8. 계층의식 - 제거
# 9. 계층이동전망 - 제거
target_count_domestic_lodgment = ['2011_50.숙박여행', '2013_46.숙박여행', '2015_국내관광여행_숙박여행횟수', '2017_국내관광여행_숙박여행횟수',
                                   '2019_국내관광여행_숙박여행횟수', '2021_국내관광여행_숙박여행횟수', '2023_국내관광여행_숙박여행횟수'] # 10. 국내 관광여행 횟수(숙박여행)

## 11. 국내 관광여행 횟수(당일여행) ~ 15. 여가활용 만족도
target_count_domestic_day = ['2011_50.당일여행', '2013_46.당일여행', '2015_국내관광여행_당일여행횟수', '2017_국내관광여행_당일여행횟수',
                              '2019_국내관광여행_당일여행횟수', '2021_국내관광여행_당일여행횟수', '2023_국내관광여행_당일여행횟수'] # 11. 국내 관광여행 횟수(당일여행)
# 12. 국내 관광여행 횟수(합) - 생략
target_count_international = ['2011_51.관광', '2013_47.관광', '2015_해외여행경험_관광횟수', '2017_해외여행경험_관광횟수', '2019_해외여행경험_관광횟수', '2021_해외여행경험_관광횟수', '2023_해외여행경험_관광횟수'] # 13. 해외여행 경험 횟수(관광)
# 14. 여가활용동반자 - 제거
# 15. 여가활용 만족도 - 제거

## 16. 소득 ~ 20. 고용의 안정성
# 16. 소득(주관적) - 제거
# 17. 소득 만족도 - 제거
# 18. 소비생활 만족도 - 제거
# 19. 직업 선택요인 1순위 - 제거
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
# 28. 거처 종류 - 제거
# 29. 점유 형태 - 제거
target_priority_work_life = ['2011_66.일과 가정생활의 우선도', '2013_62.일과가정생활의우선', '2015_일가정생활우선도코드', '2017_일가정생활우선도코드', '2019_일가정생활우선도코드', '2021_일가정생활우선도코드', '2023_일가정생활우선도코드'] # 30. 일과 가정생활의 우선도

## 31. 긴축소비지출 1순위 ~ 35. 긴축소비지출 2순위
target_austerity_consume_first = ['2011_58.긴축소비 지출항목_1순위', '2013_54.긴축소비지출항목1순위', '2015_긴축소비지출항목_1순위코드', '2017_긴축소비지출항목_1순위코드', '2019_긴축소비지출항목_1순위코드', '2021_긴축소비지출항목_1순위코드', '2023_긴축소비지출항목_1순위코드'] # 31. 긴축소비지출 1순위
target_is_domestic = ['2011_50.국내 관광여행 횟수', '2013_46.국내여행경험(지난1년간)', '2015_국내관광여행경험여부', '2017_국내관광여행경험여부', '2019_국내관광여행경험여부', '2021_국내관광여행경험여부', '2023_국내관광여행경험여부'] # 32. 국내여행여부
target_is_international = ['2011_51.지난1년간 해외 경험여부', '2013_47.해외여행경험(지난1년간)', '2015_해외여행경험여부', '2017_해외여행경험여부', '2019_해외여행경험여부', '2021_해외여행경험여부', '2023_해외여행경험여부'] # 33. 해외여행여부
# 34. 여행 횟수(합계) - 생략
target_austerity_consume_second = ['2011_58.긴축소비 지출항목_2순위', '2013_54.긴축소비지출항목2순위', '2015_긴축소비지출항목_2순위코드', '2017_긴축소비지출항목_2순위코드', '2019_긴축소비지출항목_2순위코드', '2021_긴축소비지출항목_2순위코드', '2023_긴축소비지출항목_2순위코드'] # 35. 긴축소비지출 2순위

## 36. 긴축소비지출 3순위 ~ 40. 연령 그룹
target_austerity_consume_third = ['2011_58.긴축소비 지출항목_3순위', '2013_54.긴축소비지출항목3순위', '2015_긴축소비지출항목_3순위코드', '2017_긴축소비지출항목_3순위코드', '2019_긴축소비지출항목_3순위코드', '2021_긴축소비지출항목_3순위코드', '2023_긴축소비지출항목_3순위코드'] # 36. 긴축소비지출 3순위
target_disabled_welfarecard = ['2011_14.장애인복지카드 소유여부', '2013_13.장애인복지카드소유', '2015_장애인복지카드_소유여부', '2017_장애인복지카드_소유여부', '2019_장애인복지카드_소유여부', '2021_분류코드_장애인복지카드_소유여부', '2023_장애인복지카드_소유여부'] # 37. 장애인복지카드 소유여부
# 38. 나이 제곱 - 생략
# 39. 여행 선호도 - 생략
# 40. 연령 그룹 - 생략

## 41. 근로여건만족도-근로시간 ~ 45. 근로여건만족도-인사관리
target_satisfy_working_time= ['2011_72.근로시간', '2013_68.근로여건만족도(근로시간)', '2015_근로여건만족도_근로시간코드', '2017_근로여건만족도_근로시간코드', '2019_근로여건만족도_근로시간코드', '2021_근로여건만족도_근로시간코드', '2023_근로여건만족도_근로시간코드'] # 41. 근로여건만족도-근로시간
target_satisfy_working_environment= ['2011_72.근무환경', '2013_68.근로여건만족도(근무환경)', '2015_근로여건만족도_근무환경코드', '2017_근로여건만족도_근무환경코드', '2019_근로여건만족도_근무환경코드', '2021_근로여건만족도_근무환경코드', '2023_근로여건만족도_근무환경코드'] # 42. 근로여건만족도-근무환경
target_satisfy_people_relation= ['2011_72.인간관계', '2013_68.근로여건만족도(인간관계)', '2015_근로여건만족도_인간관계코드', '2017_근로여건만족도_인간관계코드', '2019_근로여건만족도_인간관계코드', '2021_근로여건만족도_인간관계코드', '2023_근로여건만족도_인간관계코드'] # 43. 근로여건만족도-인간관계
target_satisfy_working_education= ['2011_72.직장내 교육훈련의 기회', '2013_68.근로여건만족도(교육훈련기회)', '2015_근로여건만족도_직장내교육훈련기회코드', '2017_근로여건만족도_직장내교육훈련기회코드', '2019_근로여건만족도_직장내교육훈련기회코드', '2021_근로여건만족도_직장내교육훈련기회코드', '2023_근로여건만족도_직장내교육훈련기회코드'] # 44. 근로여건만족도-직장내교육훈련
target_satisfy_manage_human_resource= ['2011_72.인사관리', '2013_68.근로여건만족도(인사관리)', '2015_근로여건만족도_인사관리코드', '2017_근로여건만족도_인사관리코드', '2019_근로여건만족도_인사관리코드', '2021_근로여건만족도_인사관리코드', '2023_근로여건만족도_인사관리코드'] # 45. 근로여건만족도-인사관리

## 46. 근로여건만족도-업무 ~ 50. 직업코드
target_satisfy_working= ['2011_72.하는 일', '2013_68.근로여건만족도(하는일)', '2015_근로여건만족도_업무코드', '2017_근로여건만족도_업무코드', '2019_근로여건만족도_업무코드', '2021_근로여건만족도_업무코드', '2023_근로여건만족도_업무코드'] # 46. 근로여건만족도-업무
target_satisfy_working_welfare= ['2011_72.복리후생', '2013_68.근로여건만족도(복리후생)', '2015_근로여건만족도_복리후생코드', '2017_근로여건만족도_복리후생코드', '2019_근로여건만족도_복리후생코드', '2021_근로여건만족도_복리후생코드', '2023_근로여건만족도_복리후생코드'] # 47. 근로여건만족도-복리후생
target_satisfy_wage_worker= ['2011_72.근로시간', '2013_66.임금근로자분류(상용,임시.일용)', '2015_임금근로자구분코드', '2017_임금근로자구분코드', '2019_임금근로자구분코드', '2021_임금근로자구분코드', '2023_임금근로자구분코드'] # 48. 임금근로자
target_worker_industry= ['2011_68.산업코드', '2013_64.산업코드', '2015_직장산업대분류코드', '2017_직장산업대분류코드', '2019_직장산업대분류코드', '2021_직장산업대분류코드', '2023_직장산업대분류코드'] # 49. 산업코드
target_worker_job= ['2011_69.직업코드', '2013_65.직업코드', '2015_직업대분류코드', '2017_직업대분류코드', '2019_직업대분류코드', '2021_직업대분류코드', '2023_직업대분류코드'] # 50. 직업코드

# 새로운 데이터프레임 생성
refined_data = pd.DataFrame({})

# 새로운 column 생성

# 0. 연도
refined_data['year'] = data[target_year].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 1. 성별 ~ 5. 전반적인 생활 여건
refined_data['sex'] = data[target_sex].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['age'] = data[target_age].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['education'] = data[target_education].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 4
# 5

## 6. 생활여건변화_문화여가생활여건 ~ 10. 국내 관광여행 횟수(숙박여행)
# 6
refined_data['is_prepared_old'] = data[target_is_prepared_old].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 8
# 9
refined_data['count_domestic_lodgment'] = data[target_count_domestic_lodgment].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 11. 국내 관광여행 횟수(당일여행) ~ 15. 여가활용 만족도
refined_data['count_domestic_day'] = data[target_count_domestic_day].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 12
refined_data['count_international'] = data[target_count_international].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 14
# 15

## 16. 소득(주관적) ~ 20. 고용의 안정성
# 16
# 17
# 18
# 19
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
# 28
# 29
refined_data['priority_work_life'] = data[target_priority_work_life].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 31. 긴축소비지출 1순위 ~ 34. 여행 횟수(합계)
refined_data['austerity_consume_first'] = data[target_austerity_consume_first].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['is_domestic'] = data[target_is_domestic].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['is_international'] = data[target_is_international].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 34
refined_data['austerity_consume_second'] = data[target_austerity_consume_second].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 36. 긴축소비지출 3순위 ~ 37. 장애인복지카드 소유여부
refined_data['austerity_consume_third'] = data[target_austerity_consume_third].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['disabled_welfarecard'] = data[target_disabled_welfarecard].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
# 38
# 39
# 40

## 41. 근로여건만족도-근로시간 ~ 45. 근로여건만족도-인사관리
refined_data['satisfy_working_time'] = data[target_satisfy_working_time].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_working_environment'] = data[target_satisfy_working_environment].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_people_relation'] = data[target_satisfy_people_relation].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_working_education'] = data[target_satisfy_working_education].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_manage_human_resource'] = data[target_satisfy_manage_human_resource].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 46. 근로여건만족도-업무 ~ 50. 직업코드
refined_data['satisfy_working'] = data[target_satisfy_working].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_working_welfare'] = data[target_satisfy_working_welfare].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_wage_worker'] = data[target_satisfy_wage_worker].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['worker_industry'] = data[target_worker_industry].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['worker_job'] = data[target_worker_job].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

print(refined_data)
refined_data.to_csv('RefinedData.csv', index=False, encoding='cp949') # 데이터 저장 