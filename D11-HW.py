#Day 11

import pandas as pd
q_df = pd.DataFrame([['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],columns=['Sex','Profession'])
print(q_df)

#缺失值填入字串'others'
ans1 = q_df.fillna("others")
print(ans1)
#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?
#dummy, 因為這串字串沒有順序

index = pd.get_dummies(ans1[['Profession']])
ans2 = pd.concat([ans1, index], axis=1)
print(ans2)
