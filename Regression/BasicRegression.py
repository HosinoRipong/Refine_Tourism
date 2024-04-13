import pandas as pd
import statsmodels.api as sm

# 파일 읽기
csv_file_path = 'RefinedData.csv'

# 다른 인코딩 시도
try:
    data = pd.read_csv(csv_file_path, encoding='cp949')
except UnicodeDecodeError:
    print("파일을 다른 인코딩으로 읽을 수 없습니다.")

pd.set_option('display.max_columns', None)

# 종속 변수 리스트
dependent_variables = ['count_domestic_lodgment', 'count_domestic_day', 'count_domestic_total', 'count_international']

for dependent_variable in dependent_variables:
    
    reg_data = data.copy()
    
    # 종속 변수 결측치 제거
    reg_data[dependent_variable] = reg_data[dependent_variable].dropna()

    # 독립 변수 선택
    X = reg_data.drop(columns=[dependent_variable])

    # 결측치를 해당 열의 평균값으로 대체
    X = X.fillna(X.mean())

    # 통제 변수에 상수 추가
    X = sm.add_constant(X)
    
    # 각 독립 변수와 종속 변수의 조합별로 선형 회귀 수행 및 결과 저장
    for independent_variable in X.columns:

        # 종속 변수 결측치 제거
        X[independent_variable] = X[independent_variable].dropna()

        model = sm.OLS(reg_data[dependent_variable], X[independent_variable]).fit()
        print(f"\n{independent_variable}, {dependent_variable} 회귀 결과:")
        print(model.summary())
        
        # 회귀 결과를 파일에 저장
        with open(f"log_results.txt", 'a') as f:
            f.write(model.summary().as_text())