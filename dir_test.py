# import os
# print(os.path.abspath('.') )# 输出当前所在绝对路径的位置
# print(os.path.abspath('..'))# 输出当前路径的上一级
# print(os.path.exists('D:/')) # 判断D盘下的目录是否存在
# print(os.path.isfile('D:/')) # 判断D盘是否为文件
#
# os.path.join('D;/','c/d') # 拼接两个路径

from pathlib import Path
p = Path('.')
print(p.resolve()) # 取得当前位置的路径

p.is_dir() # 判断某个位置是不是文件
# 创建新路径
q = Path('E:/pppython/dsfk')
Path.mkdir(q,parents = True) # parents 表示若无法创建直接到达的目录，是否可以自动创建中间文件夹