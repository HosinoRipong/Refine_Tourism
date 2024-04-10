import pandas as pd

data = pd.read_csv("IntegrateData.csv", encoding='cp949')

# 타겟 변수 설정

## 1. 성별 ~ 5. 전반적인 생활 여건
target_sex = ['2011_3. 성별', '2013_1.성별', '2015_성별코드', '2017_성별코드', '2019_성별코드', '2021_성별코드', '2023_성별코드'] # 1. 성별
target_age = ['2011_만연령', '2013_2.만나이', '2015_만연령', '2017_만연령', '2019_만연령', '2021_만연령', '2023_만연령'] # 2. 만연령
target_education = ['2011_6-1. 교육정도', '2013_4.교육정도', '2015_교육정도코드', '2017_교육정도코드', '2019_교육정도코드', '2021_교육정도코드', '2023_교육정도코드'] # 3. 교육정도
target_satisfied = ['2011_8. 주관적 만족감', '2013_6.주관적만족감', '2015_분류코드_주관적만족감코드', '2017_주관적만족감코드', '2019_주관적만족감코드', '2021_주관적만족감코드', '2023_주관적만족감코드'] # 4. 주관적만족감
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
target_satisfy_leisure = ['2011_54.여가활동 만족도', '2013_49.여가활용만족도', '2015_여가활용만족도코드', '2017_여가활용만족도코드', '2019_여가활용만족도코드', '2021_여가활용만족도코드', '2023_여가활용만족도코드'] # 15. 여가활용 만족도

## 16. 소득 ~ 20. 고용의 안정성
target_income = ['2011_55-1.실제 소득수준', '2013_51.주관적 소득수준', '2015_주관적소득수준코드', '2017_주관적소득수준코드', '2019_주관적소득수준코드', '2021_주관적소득수준코드', '2023_주관적소득수준코드'] # 16. 소득
target_satisfy_income = ['2011_59.만족도', '2013_55.소득만족도', '2015_소득만족도코드', '2017_소득만족도코드', '2019_소득만족도코드', '2021_소득만족도코드', '2023_소득만족도코드'] # 17. 소득 만족도
target_satisfy_consume = ['2011_60.소비생활 만족도', '2013_56.소비생활만족도', '2015_소비생활만족도코드', '2017_소비생활만족도코드', '2019_소비생활만족도코드', '2021_소비생활만족도코드', '2023_소비생활만족도코드'] # 18. 소비생활 만족도
target_factor_job = ['2011_61.직업선택요인_1순위', '2013_57.직업선택요인1순위', '2015_직업선택요인_1순위코드', '2017_직업선택요인_1순위코드', '2019_직업선택요인_1순위코드', '2021_직업선택요인_1순위코드', '2023_직업선택요인_1순위코드'] # 19. 직업 선택요인 1순위
target_stability_hire = ['2011_67.고용의 안정성', '2013_63.고용의안정성', '2015_고용안정성코드', '2017_고용안정성코드', '2019_고용안정성코드', '2021_고용안정성코드', '2023_고용안정성코드'] # 20. 고용의 안정성

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
refined_data['satisfy_leisure'] = data[target_satisfy_leisure].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

## 16. 소득 ~ 20. 고용의 안정성
refined_data['income'] = data[target_income].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_income'] = data[target_satisfy_income].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['satisfy_consume'] = data[target_satisfy_consume].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['factor_job'] = data[target_factor_job].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
refined_data['stability_hire'] = data[target_stability_hire].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

print(refined_data)
refined_data.to_csv('RefinedData.csv', index=False, encoding='cp949') # 데이터 저장 