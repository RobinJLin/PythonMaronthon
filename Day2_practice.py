# Day 2 
import numpy as np
#see python shell 

##1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
print(array1)

print(array1.reshape(5,6))

#2.呈上題的array，找出被6除餘1的數的索引

array2 = array1.reshape(5,6) 

print(np.where(array2%6 == 1, "Y", "N"))