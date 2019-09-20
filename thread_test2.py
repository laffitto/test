import threading
from threading import current_thread  # 方法特别长时，建议用from...import的形式


class Mythread(threading.Thread): # 此处threading.Thread后不加括号，使用的是Thread方法的名称，而不是引用
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')

t1 = Mythread() # 进行实例化，要加括号
t1.start()
t1.join() # 目的是不让主线程先结束

print(current_thread().getName(),'end')
