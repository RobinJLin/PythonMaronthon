#Day 8

import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolen]

dt = np.dtype({'names':('name', 'sex', 'weight', 'rank', 'mytopia'), 'formats':((np.str_, 5), (np.str_, 5), np.float_, np.int_, np.bool_)})
#dt = np.dtype('U, U, f8, i, ?')
cal = np.zeros(8, dtype=dt)
cal["name"] = name_list
cal["sex"] = sex_list
cal["weight"] = weight_list
cal["rank"] = rank_list
cal["mytopia"] = myopia_list

print(cal)

#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重

weights = cal['weight']
meanWeights = np.mean(weights)
print("全部平均體重為{}".format(meanWeights))

#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重
print(cal[cal['sex']=='boy']['weight'])
print("男生平均體重{}".format(np.mean(cal[cal['sex']=='boy']['weight'])))

#3. 呈上題，進一步算出女生(sex欄位是girl)平均體重

print(cal[cal['sex']=='girl']['weight'])
print("女生平均體重{}".format(np.mean(cal[cal['sex']=='girl']['weight'])))