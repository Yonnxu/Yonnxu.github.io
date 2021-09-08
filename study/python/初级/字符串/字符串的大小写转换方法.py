s = 'hello,python'
print('原id', s, id(s))
# 转成大写之后，会产生一个新的字符串对象

a = s.upper()
print('使用upper全部转换大写', a, id(a))

# 转换之后，会产生一个新的字符串对象
b = s.lower()
print('使用lower全部转换为小写', b, id(b))
print(s, id(s))
print(b == s)
print(b is s)  # False

s2 = 'hello.Pvthon'
print('使用swapcase()大写变小写,小写变大写', s2.swapcase())
print('使用title()每个字符开头大写,剩余的小写', s2.title())
