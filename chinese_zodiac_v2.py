# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊' # 字符串
# chinese_zodiac = 'fuckyoubitch'
# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])

# year = int(input('请用户输出出生年份'))
# if(chinese_zodiac[year % 12]) == '狗':
#     print('狗年大吉')
# print(chinese_zodiac[year % 12])

# for cs in chinese_zodiac:
#     print(cs)
#
# for i in range(13):
#     print(i)

# for year in range(2000,2020):
#     print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))

# num = 5
# while True:
#     print('a')
#     num = num +1
#     if num > 10:
#         break

import time
num = 5
while True:
    num = num +1
    if num ==10:
        continue # 跳出此次循环
    print(num)
    time.sleep(1)