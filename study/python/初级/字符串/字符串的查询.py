s = 'hello,hello'
# 建议用find方法
# 查找第一次出现的位置  不存在则抛出ValueError
print(s.index('lo'))

# 查找第一次出现的位置 不存在抛出-1
print(s.find('lo'))

# 查找最后一次出现的位置  不存在则抛出ValueError
print(s.rindex('lo'))

# 查找最后一次出现的位置  不存在抛出-1
print(s.rfind('lo'))
