s = 'hello.Python'
# 第一个参数指定长度，第二个参数不写默认是空格
print(s.center(20, '*'))  # 居中对齐
print(s.ljust(20, '*'))  # 左对齐
print(s.ljust(10))
print(s.ljust(20))

print(s.rjust(20, '*'))  # 右对齐
print(s.rjust(20))
print(s.rjust(10))

print(s.zfill(20))  # 右对齐，使用0进行填充 不能指定第二个参数
print(s.zfill(10))
print('-1543'.zfill(8))