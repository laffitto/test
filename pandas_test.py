from pandas import Series,DataFrame
import pandas as pd

obj = Series([4,5,6,-7]) # 对numpy的array进行封装,前面自动增加索引
# print(obj)
# print(obj.index) # 索引
# print(obj.values) # 值

# obj2 = Series([4,7,-5,4],index = ['d','b','c','a']) # 手动添加索引
# print(obj2)
# obj2['c'] = 6 # 对索引赋值
# print(obj2)
# print('a' in obj2) # 判断a是否存在于索引之中

# date = {'a': 1, 'b': 2, 'c': 3 , 'd':4} # 将字典直接转化为Series
# obj3 = Series(date)
# print(obj3)
#
# obj3.index = ['z','y','x','w'] # 修改索引的名称
# print(obj3)

# data = {'city':['beijing','shanghai','nanjing','tianjing','hefei'],
#         'year':[2015,2016,2017,2018,2019],
#         'pop':[1.4,1.3,1.5,2.6,3.6]}
#
# frame = DataFrame(data)
#
# frame2 = DataFrame(data,columns=['year','city','pop']) # 根据特定规则排序后进行输出
# print(frame)
# print(frame2)
#
# print(frame2['city'])  # 提取特定数组的2种方法，变成一维的数据
# print(frame2.year)
#
# frame2['new'] = 100  # 生成新的一列
# print(frame2)

# frame2['capital'] = frame2.city == 'beijing' # 生成新的一列判断city是否为beijing
# print(frame2)

# pop = { 'beijing':{2018:1.5, 2019:2.0},
#         'shanghai':{2018:1.6, 2019:2.4}
#         }
# frame3 = DataFrame(pop)
# print(frame3)
#
# print(frame3.T) # 转置

# obj4 = Series([4.5, 7.3, -5.6, 4.2], index=['d', 'b', 'c', 'a'])
#
# obj5 = obj4.reindex(['a','b','c','d','e'],fill_value=0) # 按照索引重新排序,并将新的值设为0
# print(obj5)
#
# obj6 = Series(['blue','red','yellow'],index = [0,2,4])
#
# print(obj6.reindex(range(6),method= 'ffill')) # 重新排序，缺省值按照上面的数值填充
# print(obj6.reindex(range(6),method= 'bfill')) # 用下面的数值进行填充

# from numpy import nan as NA
#
# data = Series([1,NA,2])
# print(data.dropna()) # 删除有NA的缺失值
#
# data2 = DataFrame([[1,2.3,3],[2,NA,NA],[NA,NA,NA]])
# data2[4] = NA
# print(data2)
# print(data2.dropna(how = 'all')) # 将某一行都是缺失值的行删除
# print(data2.dropna(axis= 1 ,how = 'all'))  # 将某一列都是缺失值的列删除
#
# data2.fillna(0) # 将缺失值都赋为0
# print(data2.fillna(0))
import numpy as np
data3 = Series(np.random.randn(10),
               index = [['a','a','a','b','b','b','c','c','d','d'],
                        [1,2,3,1,2,3,1,2,2,3]])
print(data3)

print(data3['b':'c']) # 输出b与c的索引

print(data3.unstack()) # 将一维的Series转化为二维的DataFrame
print(data3.unstack().stack()) # 转化回来
