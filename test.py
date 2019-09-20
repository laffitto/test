import re

# p = re.compile('ca*t') # 要进行匹配的字符串
# print(p.match('caaaat'))       # 需要被匹配的字符串
#
# p = re.compile('...')
# print(p.match('cat'))
#
# p = re.compile('.{3}')  # 通过组合达到与上面相同的效果
# print(p.match('cat'))

# # \d匹配连续字符,（）表示进行分组，r 表示告诉后面内容进行原样输出，而不进行转义
# p = re.compile(r'(\d+)-(\d+)-(\d+)') # +表示匹配连续的数字，让此处06或6都可以匹配上
# print(p.match('2019-06-11'))
# print(p.match('2019-06-11').group()) # group 表示取出匹配的一部分
# print(p.match('2019-06-11').group(1)) # 取出第一个括号包括的部分
# print(p.match('2019-06-11').groups()) # 取出匹配的所有部分
#
# year, month, day = p.match('2019-06-11').groups() # 将匹配部分映射给对应量
# print(month)

phone = '123-456-789 # 这是电话号码'
p = re.sub(r'#.*$','',phone) # 将#号后面字符替换为空字符串
print(p)
p2 = re.sub(r'\D','',p) # 将其他符合替换成空字符串
print(p2)
