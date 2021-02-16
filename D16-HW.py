#Day 16
import numpy as np
import pandas as pd
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)
series

#1. 將所有轉為周資料
print(series)

print(series.to_period(freq="W"))

#2. 將周資料的值取平均

#這邊要用 resample() 因為resample 會把我們要的時間長度組合一起
print(series.resample("W").mean())
#dataWeek.groupby('Freq')