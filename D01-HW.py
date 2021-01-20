import numpy as np


#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
c = np.arange(1,21,1)
print(c)


#2.呈上題，將以上數列取出偶數。

print(c[1:20:2])

#3.呈1題，將數列取出3的倍數

print(c[2:20:3])