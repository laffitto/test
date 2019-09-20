def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding data
    """
path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0] # 返回'ads'
table = path.split('//')[1].split('/')[1] # 返回 'training_table'
qqq = path.split('//')[0]
data = query_data(namespace, table)
print(data)
print(namespace)
print(table)
print(qqq)

# import time
# start_time = time.time()
# s = ''
# for n in range(0, 1000000):
#     s += str(n)
# end_time = time.time()
# print(end_time-start_time)
# start_time1 = time.time()
# l = []
# for n in range(0, 1000000):
#     l.append(str(n))
# s = ' '.join(l)
# end_time1 = time.time()
# print(end_time1-start_time1)

# print('no data available for person with id: {123},name: {tom}')
# print('no data available for person with id: {}, name: {}'.format('123', 'tom'))