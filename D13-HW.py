#Day 13

import pandas as pd
score_df = pd.DataFrame([[1,56,66,70], 
              [2,90,45,34],
              [3,45,32,55],
              [4,70,77,89],
              [5,56,80,70],
              [6,60,54,55],
              [7,45,70,79],
              [8,34,77,76],
              [9,25,87,60],
              [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
score_df = score_df.set_index('student_id')
print(score_df)

#1.6號學生(student_id=6)3科平均分數為何?

print(score_df.iloc[[5]].mean(axis=1))


#2. 6號學生3科平均分數是否有贏過班上一半的同學
mean_score = score_df.mean(axis=1)
print(mean_score.sort_values())

#有

#由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問6號同學3科成績分別是?

new_score = score_df.iloc[[5]].apply(lambda x : x**(0.5)*10)
print(new_score)

#承上題，加分後各科班平均變多少
new_score_all = score_df.apply(lambda x : x**(0.5)*10)
new_mean = new_score_all.mean()

#print(new_mean)
print(f"數學是{round(new_mean.loc['math_score'], 2)}", f"英文是{round(new_mean.loc['english_score'], 2)}", f"國文是{round(new_mean.loc['chinese_score'], 2)}")