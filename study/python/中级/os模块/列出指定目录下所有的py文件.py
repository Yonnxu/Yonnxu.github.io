import os

# 返回当前的工作目录
path = os.getcwd()

# 返回指定路径 下的文件和目录信息
lst = os.listdir(path)

# 遍历
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
