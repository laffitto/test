# import numpy as np
# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print (np.percentile(a, 50))
# print (np.percentile(a, 50, axis=0))
# print (np.percentile(a, 50, axis=1))

import pandas as pd
from pandas import Series, DataFrame
# df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# print (df1.describe())

# df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(5)})
# df3 = pd.merge(df1, df2, on='name')  # 基于name这列进行连接
#
# # inner内链接是merge合并的默认情况，inner内连接其实也就是键的交集，在这里df1, df2相同的键是name，所以是基于name字段做的连接
# df4 = pd.merge(df1, df2, how='inner')
# df5 = pd.merge(df1, df2, how='left')  # 左连接，以第一个DataFrame为主进行的连接，第二个DataFrame作为补充。
# df6 = pd.merge(df1, df2, how='right') # 右连接，以第二个DataFrame为主进行的连接，第一个DataFrame作为补充。
# df7 = pd.merge(df1, df2, how='outer') # 外连接相当于求两个DataFrame的并集。
# print(df3)
# print(df4)
# print(df5)
# print(df6)
# print(df7)

scores = {'Chinese': [66, 95, 95, 90, 80, 80],
'English': [65, 85, 92, 80, 90, 90],
'Math': [None, 98, 96, 77, 90, 90]}
df = DataFrame(scores, index=['Zhang Fei', 'Guan Yu', 'Zhao Yun', 'Huang Zhong', 'Dian Wei','Dian Wei'])
df = df.drop_duplicates()
print(df)
df['title'] = df.sum(axis = 1)
print(df)