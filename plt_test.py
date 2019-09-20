import matplotlib.pyplot as plt

# plt.plot((1,3,5),(2,6,7)) # 绘制简单曲线
# plt.show()

import numpy as np

# x = np.linspace(-np.pi,np.pi,100) # x输入的定义域为-pi到pi，中间间隔100个元素
# plt.plot(x,np.sin(x))
# plt.show()
#
# x = np.linspace(-np.pi * 2,np.pi * 2,100)
# plt.figure(1,dpi=50)
# for i in range (1,5):
#     plt.plot(x,np.sin(x/i))
# plt.show()

# plt.figure(1,dpi=50) # 创建图表1，dpi表示图片精细度，dpi越大文件越大
# data = [1,1,2,3,4,3,5,6,7,7,3]
# plt.hist(data) # 只要传入数据，直方图就会统计数据出现的次数
# plt.show()

x = np.arange(1,10)
y = x
fig = plt.figure()
plt.scatter(x,y,c = 'r', marker= 'o') # 散点颜色为红色，形状为圆形
plt.show()