'''
getcwd()                                 返回当前的工作目录

listdir(path)                            返回指定路径 下的文件和目录信息

mkdir(path[, mode])                      创建目录

makedirs(path1/path2... [, mode])        创建多级目录

rmdir(path)                              删除目录

removedirs(path1/path......)             删除多级目录

chdir(path)                              将path设置为当前工作目录
'''

# os模块与操作系统相关的一个模块


import os
# 调用记事本
# os.system('notepad.exe')

# 调用计算机
# os.system('calc.exe')

# 直接调用可执行文件
# os.startfile('F:\KuGou\Fall Out Boy - My Songs Know What You Did In the Dark (Light Em Up).mp3')

# 返回当前的工作目录
print(os.getcwd())

# 返回指定路径 下的文件和目录信息
lst = os.listdir('../元组')
print(lst)

# 创建目录
os.mkdir('mkdir1')

# 创建多级目录
os.makedirs('A/B/C')

# 删除目录
os.rmdir('mkdir1')

# 删除多级目录
os.removedirs('A/B/C')

# 将path设置为当前工作目录
os.chdir()