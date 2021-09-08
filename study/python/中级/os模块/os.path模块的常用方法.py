'''
abspath(path)                      用于获取文件或目录的绝对路径

exists(path)                       用于判断文件或目录是否存在，如果存在返回True,否则返回False

join(path,name)                    将目录与目录或者文件名拼接起来

splitext()                         分离文件名和扩展名

basename(path)                     从一个目录中提取文件名

dirname(path)                      从一个路径中提取文件路径，不包括文件名

isdir(path)                        用于判断是否为路径
'''

import os.path

# 用于获取文件或目录的绝对路径
print(os.path.abspath('os.txt'))

# 用于判断文件或目录是否存在，如果存在返回True,否则返回False
print(os.path.exists('os.txt'), os.path.exists('os模块的常用函数.py'))

# 将目录与目录或者文件名拼接起来
print(os.path.join('E:\PyCharm 2019.2.5', 'demo.py'))

# 分离文件路径和文件名
print(os.path.split('E:\\PyCharm 2019.2.5\\project\\中级\\os模块\\os模块的常用函数.py'))

# 分离文件名和扩展名
print(os.path.splitext('E:\\PyCharm 2019.2.5\\project\\中级\\os模块\\os模块的常用函数.py'))

# 从一个目录中提取文件名
print(os.path.basename('E:\\PyCharm 2019.2.5\\project\\中级\\os模块\\os模块的常用函数.py'))

# 从一个路径中提取文件路径，不包括文件名
print(os.path.dirname('E:\\PyCharm 2019.2.5\\project\\中级\\os模块\\os模块的常用函数.py'))

# 判断是否为路径
print(os.path.isdir('E:\\PyCharm 2019.2.5\\project\\中级\\os模块\\os模块的常用函数.py'))
print(os.path.isdir('E:\\PyCharm 2019.2.5\\project\\中级\\os模块'))