#Day 12

#HW
import pandas as pd
import numpy as np
from matplotlib.pyplot import plot, show
#1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?

bostonCSV = pd.read_csv("data/boston.csv")
print(bostonCSV)

#箱型圖
df = pd.DataFrame(bostonCSV)
print(df)
df.boxplot()
show()

#B 和TAX 的中位數300-400間


#2. 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
df = pd.DataFrame(bostonCSV, columns=["NOX","DIS"])
print(df)
df.plot.scatter(x='NOX', y='DIS')
show()

#有點負相關


#notes
#from matplotlib.pyplot import plot, show
#x = range(10)
#plot(x)
#show()
#y = [2, 8, 3, 9, 4] * 2
#plot(y)

#import pandas as pd
#import numpy as np
#from matplotlib.pyplot import plot, show

#ts = pd.Series(np.random.randn(200), index=pd.date_range('1/1/2020', periods=200))
#ts = ts.cumsum()
#print(ts)
#ts.plot()
#show() #using wingpro IDE

#df = pd.DataFrame(np.random.randn(200, 3), index=pd.date_range('1/1/2020', periods=200), columns=["A","B","C"])
#df = df.cumsum()
#print(df)
#df.plot();

#show()
