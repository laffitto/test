class Testwith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:  # 若无异常，exc_tb的值为None
            print('正常结果')
        else:
            print('has error %s' %exc_tb)



with Testwith():
    print('Test is running')
    raise NameError('testNameError') # 特意在程序中制造出异常