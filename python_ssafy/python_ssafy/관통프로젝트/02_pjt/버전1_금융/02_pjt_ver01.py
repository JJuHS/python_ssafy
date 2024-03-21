import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# A. DATA 읽어오기
selected_col = ['Date', 'Open', 'High', 'Low', 'Close']
data = pd.read_csv('NFLX.csv', usecols=selected_col)

# B. 2021년 이후 종가 데이터 시각화하기
data['Date'] = pd.to_datetime(data['Date'])
data_after_2021 = data[data['Date'].dt.year >= 2021]

plt.plot(data_after_2021['Date'], data_after_2021['Close'])
plt.xlabel('Date')
plt.xticks(rotation = 45)
plt.ylabel('Close Price')
plt.title('NetFlix Close Price')
plt.show()

# C. 2021년 이후 최고/최저 종가 출력하기
min_price = data_after_2021['Close'].min()
max_price = data_after_2021['Close'].max()

print(f'최고 종가 : {max_price}')
print(f'최저 종가 : {min_price}')

# D. 2021년 이후 월별 평균 종가 출력하기
month_mean_close = data_after_2021.groupby(data_after_2021['Date'].dt.to_period('M'))['Close'].mean()

plt.plot(month_mean_close.index.strftime('%Y-%m'), month_mean_close)

plt.xlabel('Date')
plt.xticks(rotation = 45)
plt.ylabel('Average Close Price')
plt.title('Montly Average Close Price')
plt.xticks([0,2,4,6,8,10,12])
plt.show()

# E. 2022년 이후 최고, 최저, 종가 시각화하기
data_after_2022 = data[data['Date'].dt.year >= 2022]
plt.plot(data_after_2022['Date'], data_after_2022['High'], label = 'High')
plt.plot(data_after_2022['Date'], data_after_2022['Low'], label = 'Low')
plt.plot(data_after_2022['Date'], data_after_2022['Close'], label = 'Close')
plt.title('High, Low, and Close Price since January 2022')
plt.xlabel('Date')
plt.xticks(rotation = 45)
plt.ylabel('Price')
plt.legend()
plt.show()



