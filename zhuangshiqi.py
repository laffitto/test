# def pocl(ppp):
#     print('m is my {}'.format(ppp))
#
# ketl = pocl('bitch')
# print(ketl)

def my_decorator(func):
    def wrapper(*arg, **kwargs):
        print('wrapper of decorator')
        func(*arg, **kwargs)
    return wrapper

@my_decorator
def adds(a,b):
    print(a+b)

adds(1,2)