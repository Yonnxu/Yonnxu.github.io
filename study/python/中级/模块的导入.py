# 导入模块
# import   模块名称    [as别名]
# from     模块名称    import    函数/变量/类


import math

print(id(math))
print(type(math))
print(math)
print(math.pi)
print('-------------------------------')
print(dir(math))
print(math.pow(2, 3), type(math.pow(2, 3)))  # 2的三次方
print(math.ceil(9.00001))  # 最大的
print(math.floor(9.999))  # 最小的
print('-------------------------------')

from math import pi  # 只能用pi方法 其他的如果要用需要重新导入 import math

print(pi)
