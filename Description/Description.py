import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('RefinedData.csv')

# 각 column에 대해 기술통계량 계산
statistics = data.describe()

# 각 column에 대해 Box plot 그리기
plt.figure(figsize=(10, 6))
data.boxplot()
plt.title('Box Plot for each column')
plt.xlabel('Columns')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()

# 결과 출력
print("기술통계량:")
print(statistics)

# CSV 파일로 저장
statistics.to_csv('statistics2.csv')
print("기술통계량이 statistics.csv 파일로 저장되었습니다.")