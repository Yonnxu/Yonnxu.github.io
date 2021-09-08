s = 'hello world Python'
# split()————从字符串的左边开始劈分，默认的劈分字符是空格字符串,返回的值都是一个列表
# 可以通过参数sep指定劈分字符串是的劈分符
lst = s.split()
print(lst)

s1 = 'hello world Python'
print(s1.split())
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))
