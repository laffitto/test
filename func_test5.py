def new_tips(argv):    # 里面不动，再在外面封装一层
    def tips(func):
        def nei(a, b):
            print(
                'start %s %s' %
                (argv, func.__name__))  # func.__name__ 表示取函数的名称
            func(a, b)
            print('stop')
        return nei
    return tips


@new_tips('add_moudle')
def add(a, b):
    print(a + b)


@new_tips('sub_moudle')
def sub(a, b):
    print(a - b)


print(add(4, 5))
print(sub(4, 5))
