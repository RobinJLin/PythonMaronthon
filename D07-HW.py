#Day 7
import numpy as np


#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1 = np.array([[10, 8], [3, 5]])
array1_inv = np.linalg.inv(array1)

new_array = array1@array1_inv

print(new_array) #單位矩陣

#2. 運用上列array計算特徵值、特徵向量?

w, v = np.linalg.eig(new_array)

#特徵值 eigenvalues 
print(w)

#特徵向量 （eigenvector) 
print(v)

#3. 運用上列array計算SVD?

u, s, vh = np.linalg.svd(new_array)
print(u)
print(s)
print(vh)