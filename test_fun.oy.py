# var1 = 123
#
# def func():
#     global var1
#     var1 = 456
#     print(var1)
#
# func()
# print(var1)

# iter() next()

# list1 = [1,2,3]
# it = iter(list1)
# print ( next(it))
# print ( next(it))
# print ( next(it))
# print ( next(it)) # except

# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
# for i in frange(10,20,0.5):
#     print(i)

# def add (x,y): return x+y
# lambda  x,y: x+y
#
# lambda x:x<= (month,day)
#
# def func1(x):
#     return x<= (month,day)
#
# lambda  item: item[1]

def func2(item):
    return item[1]

adict = {'a':'aa', 'b':'bb'}
for i in adict.items():
    func2(i)