import sys
import time
import urllib.request

print(sys.getsizeof(24))  # 占了28个字节
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))  # 占了24个字节
print('----------------------------')

print(time.time())
print(time.localtime(time.time()))
print('----------------------------')
print(urllib.request.urlopen('http://www.baidu.com').read())