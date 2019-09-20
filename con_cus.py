from threading import Thread,current_thread
import time
import random
from queue import Queue

queue = Queue(5) # 定义队列的长度

# 生产者，经过随机时间添加数字
class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()  # 获取线程的名字
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)  # 随机选择一个数字
            queue.put(num)  # 将数字放入指定的队列中
            print('生产者 %s 生产了数据 %s' %(name, num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s秒' %(name, t))


# 消费者，经过随机时间提取数字
class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()  # 获取线程的名字
        global queue
        while True:
            num = queue.get() # 从消费者队列中取出想要的数据
            queue.task_done() # 包含线程等待与线程同步的代码，可直接调用
            print('消费者 %s 消耗了数据 %s' %(name, num))
            t = random.randint(1,5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s秒' %(name, t))

p1 = ProducerThread(name = 'p1')
p1.start()
# p2 = ProducerThread(name = 'p2')
# p2.start()
# p3 = ProducerThread(name = 'p3')
# p3.start()
c1 = ConsumerThread(name = 'c1')
c1.start()
c2 = ConsumerThread(name ='c2')
c2.start()


