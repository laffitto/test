import numpy as np
# # 可以自动判断数据类型
# arr1 = np.array([2,3,4]) # 定义一个数组
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.2,2.3,3.4])
# print(arr2)
# print(arr2.dtype)
# # 实现列表的累加
# print(arr1+ arr2)
#
# print(arr2*10)

# # 定义二维数组（矩阵）
# data = [[1,2,3],[4,5,6]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)
# # 定义0矩阵
# print(np.zeros(10)) # 一维矩阵
# print(np.zeros((3,5))) # 定义3*5 的矩阵
#
# print(np.ones((4,6))) # 全为1 的矩阵
# # 将矩阵空置（但会填充随机值）
# print(np.empty((2,3,2))) # 三维矩阵

print(np.arange(10)) # 生成数组
arr4 = np.arange(10)
print(arr4[5:8]) # 切片操作
arr4[5:8] = 10 # 切片内容赋值
print(arr4)
# 赋值而不改变原有内容
arr_slice = arr4[5:8].copy() # 添加副本
arr_slice[:]= 15
print(arr_slice)
print(arr4)