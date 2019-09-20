# i = j # NameError: name 'j' is not defined 变量错误
#
#
# print()) # SyntaxError: invalid syntax 语法错误
#
#
# a = '123'
# print(a[3]) # IndexError: string index out of range 列表错误，超过索引范围
#
# d = {'a':1, 'b': 2}
# print(d['c']) # KeyError: 'c' 字典错误
#
# year = int(input('input year:'))
# # ValueError: invalid literal for int() with base 10: 'adf' 输入类型不符合预期
#
# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('年份要输入数字')

# a = 123
# a.append() # AttributeError: 'int' object has no attribute 'append' 属性错误

# except (ValueError,AttributeError,KeyError)

# try:
#     print(1/'a')
# except Exception as d:
#     print(' %s' %d)

# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')

try:
    a = open('name.txt')
except Exception as e:
    print(e)  # 若打开文件失败对错误进行输出
finally:
    a.close() # 无论是否操作成功，都对文件进行关闭操作