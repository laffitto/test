f = open('name.txt')
data = f.read()
print(data.split('|'))

f2 = open('weapen.txt')
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1

f3 = open('sangou.txt',encoding='GB18030')
print(f3.read().replace('\n',''))