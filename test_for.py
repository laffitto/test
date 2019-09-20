# 列表推导式
# 从1到10 偶数的平方
alist = []
for i in range(1,11):
    if (i % 2 == 0):
        alist.append( i*i )

print(alist)


blist = [i*i for i in range (1,11) if (i % 2)== 0]
print(blist)


# 字典推导式
z_num = {}
for i in zodiac_name:
    z_num[i] = 0

z_num = {i:0 for i in zodiac_name}