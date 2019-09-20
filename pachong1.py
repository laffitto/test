# from urllib import request
#
# url = 'http://www.baidu.com'
# response = request.urlopen(url,timeout=1) # 打开网页并设置超时时间为1s
# print(response.read().decode('utf-8')) # 用utf-8格式进行解码

from urllib import parse
from urllib import request

# data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')



response2 = request.urlopen('http://httpbin.org/get',timeout= 1)
print(response2.read())

