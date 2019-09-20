# import time
# print(time.time()) # 1970年到现在经历的秒数
# print(time.localtime()) # 转化为年月日
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # 输出年月日，小时分钟秒


# import datetime
# print(datetime.datetime.now()) # 输出当前时间
# newtime = datetime.timedelta(minutes=10) # 10min后
# print(newtime)
# print(datetime.datetime.now() + newtime)
#
# one_day = datetime.datetime(2008,5,27)
# new_date = datetime.timedelta(days = 10) # 10天后
# print(one_day + new_date)

import random
print(random.randint(1,5)) # 随机取1到5内的整数
print(random.choice(['aa','bb','cc'])) # 随机抽取字符串

