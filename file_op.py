# 将小说主要人物记录
# file1 = open('name.txt','w') # w 表示可以写入文件，默认mode为r，即只读
# file1.write('诸葛亮')
# file1.close()
#
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt','a') # a 表示可以添加新事物
# file3.write('刘备')
# file3.close()

# file4 = open('name.txt')
# print(file4.readline()) # 仅读取一行
#
# file5 = open('name.txt')
# for line in file5.readlines(): # readlines表示逐行读取
#     print(line)
#     print('-------')

file6 = open('name.txt')
print('当前文件指针的位置%s ' %file6.tell()) # tell表示文件的指针，最开始在开头
print('当前读取到了一个字符，字符内容为 %s' %file6.read(1)) # 只读一个字符
print('当前文件指针的位置%s ' %file6.tell())

file6.seek(0)  # seek函数改变指针的位置
print('我们进行了seek的操作')
print('当前文件指针的位置%s ' %file6.tell())
print('当前读取到了一个字符，字符内容为 %s' %file6.read(1))
print('当前文件指针的位置%s ' %file6.tell())
file6.close()
# 第一个参数代表偏移的位置，第二个参数 0表示从文件开头开始偏移  1表示从当前位置偏移 2从文件结尾
file6.seek(5,0)