# replace()————第1个参数指定被替换的子串，
# 第2个参数指定替换子串的字符串,该方法返回替换后得到的字符串，替换前的字符串不发生变化,调用该方法时可以通过第3个参数指定最大替换次数
s = 'hello,Python'
print(s.replace('Python', 'Java'))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))


# join()————将列表或元组中的字符电合并成一个字符串
lst = ['hello', 'java', 'Python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'Java', 'Python')
print(''.join(t))

print('*'.join('Python'))
