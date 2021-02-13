#day 10

import pandas as pd 

#讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv
stock1 = pd.read_csv("data/STOCK_DAY_0050_202009.csv")
stock2 = pd.read_csv("data/STOCK_DAY_0050_202010.csv")
#print("stock1 is {}".format(stock1))


#串聯

stock_all = pd.concat([stock1, stock2], axis=0)
#
#print(stock_all)
#找出open小於close的資料

ans = stock_all.loc[(stock_all.open)<(stock_all.close)]
print(ans)