def func():
    a = 1
    b = 2
    return  a+b


def sum(a):
    def add(b):
        return  a+b
    return add

# add 函数的名称或函数的引用
# add() 函数的调用

num1 = func()
num2 = sum(2)
num2(4)
print(num2(4))
print(type(num1))
print(type(num2))
