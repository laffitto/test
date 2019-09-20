# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊' # 字符串

# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])

year = 2018
year % 12 # 取余数
print(chinese_zodiac[year % 12])

print ('狗' not in chinese_zodiac)

print(chinese_zodiac + chinese_zodiac)
print(chinese_zodiac + 'acdf')
print(chinese_zodiac * 4)

a_list = ['abc', 'xyz'] #列表
a_list.append('X')
print(a_list)
a_list.remove('xyz')
print(a_list)

x = 'abcd'
if x == 'abc' :
    print('相等')
else:
    print('不相等')