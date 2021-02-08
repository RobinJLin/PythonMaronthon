# Day 6 
import numpy as np

#1. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])


with open('data/two_array.npz', 'wb') as f:
    np.savez(f, array1 = array1, array2 = array2)

   

#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
npzfile = np.load('data/multi_array.npz')
#print(npzfile)
#print(npzfile.files)
#print("first file {}".format(npzfile['array1']))
#print("second file {}".format(npzfile['array2']))
#print("third file {}".format(npzfile['array3']))

two_array = np.load('data/two_array.npz')
print(two_array.files)
print(two_array['array1'])
print(two_array['array2'])
with open ('data/ans.npz', 'wb') as f:
    np.savez(f, two_array['array1'], two_array['array2'], npzfile['array1'], npzfile['array2'], npzfile['array3'])



ans = np.load('data/ans.npz', 'wb') 

print(ans["arr_0"])
print(type(ans["arr_1"][0]))