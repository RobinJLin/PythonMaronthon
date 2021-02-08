#Day 5 HW

import numpy as np
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?

#max 
#English
print(np.amax(english_score))
#math 
print(np.nanmax(math_score))
#Chinese
print(np.amax(chinese_score))

#min
#English
print(np.amin(english_score))
#math 
print(np.nanmin(math_score))
#Chinese
print(np.amin(chinese_score))

#sd
#English
print(np.std(english_score))
#math 
print(np.nanstd(math_score))
#Chinese
print(np.std(chinese_score))

#可以忽略

#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?

math_score[4] = 55
print("補考後，新的成績為{}".format(math_score))

print(math_score.mean())
print(np.mean(math_score))

print(np.amax(math_score))
print(np.amin(math_score))
print(np.std(math_score))
#3. 用補考後資料找出與國文成績相關係數最高的學科?

print(np.corrcoef(chinese_score, math_score))

print(np.corrcoef(chinese_score, english_score))

#English