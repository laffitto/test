# def addd(a,b):
#     return  a+b
#
# print(addd(34,5))
# print(addd([1,2],[2,3]))
# print(addd('hello',' world'))

# a = [(lambda x :x**2)(x) for x in range (10) ]
# print (a)

# b= [ x*x for x in range(10)]
# print(b)
#
# d = {'mike': 10, 'lucy': 2, 'ben': 30}
# c = sorted(d.items(),key = lambda x : x[1])
# print(c)

# import copy
# x = [1]
# x.append(x)
#
# y = copy.deepcopy(x)
#
# x == y

def func(d):
    d['a'] = 10
    d['b'] = 20

d = {'a': 1, 'b': 2}
func(d)
print(d)