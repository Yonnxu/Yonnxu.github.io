# 打开密码


# import os
# import time
# def Jy():
#     print('开始破解：')
#     for a in range(len(str)):
#         for b in range(len(str)):
#             for c in range(len(str)):
#                 for d in range(len(str)):
#                     myStr=str[a]+str[b]+str[c]+str[d]#生成压缩包密码
#                     #这里修改WinRAR.exe所在路径、压缩包路径和解压目录（C:\Program Files (x86)\WinRAR\WinRAR.exe、52pojie.rar、52pojie）
#                     jy=r'"C:\Program Files (x86)\WinRAR\WinRAR.exe" -ibck -y x -p%s 52pojie.zip 52pojie'%myStr
#                     if os.system(jy)==0:
#                         print('密码正确!',myStr)
#                         ent=time.time()
#                         print('破解成功！用时%f分'%((ent-stm)/60))
#                         return
#                     else:
#                         print('密码错误：',myStr)
#     ent=time.time()
#     print('破解失败，用时%f分'%((ent-stm)/60))
# stm=time.time()
# str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#这里加上你想要的字符
# if os.path.exists('52pojie')==False:#判断当前py文件所在目录下是否存在52pojie文件夹，如果没有则建立
#     os.mkdir('52pojie')
#     Jy()
# else:#存在则进行下一步
#     Jy()


# 破解解压密码

import zipfile
import time
import threading

startTime = time.time()
# 判断线程是否需要终止
flag = True


def extract(password, file):
    try:
        password = str(password)
        file.extractall(path='.', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        print("spend time is {}".format(nowTime - startTime))
        global flag
        # 成功解压其余线程终止
        flag = False
    except Exception as e:
        print(e)


def do_main():
    zfile = zipfile.ZipFile("a.zip", 'r')
    # 开始尝试
    for number in range(1, 9999):
        if flag is True:
            t = threading.Thread(target=extract, args=(number, zfile))
            t.start()
            t.join()


if __name__ == '__main__':
    do_main()



# 数组字母组合
#
# import zipfile
# import random
# import time
# import sys
#
#
# class MyIterator():
#     # 单位字符集合
#     letters = 'abcdefghijklmnopqrstuvwxyz012345678'
#     min_digits = 0
#     max_digits = 0
#
#     def __init__(self, min_digits, max_digits):
#         # 实例化对象时给出密码位数范围，一般4到10位
#         if min_digits < max_digits:
#             self.min_digits = min_digits
#             self.max_digits = max_digits
#         else:
#             self.min_digits = max_digits
#             self.max_digits = min_digits
#
#     # 迭代器访问定义
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         rst = str()
#         for item in range(0, random.randrange(self.min_digits, self.max_digits + 1)):
#             rst += random.choice(MyIterator.letters)
#         return rst
#
#
# def extract():
#     start_time = time.time()
#     zfile = zipfile.ZipFile("a.zip")
#     for p in MyIterator(5, 6):
#         try:
#             zfile.extractall(path=".", pwd=str(p).encode('utf-8'))
#             print("the password is {}".format(p))
#             now_time = time.time()
#             print("spend time is {}".format(now_time - start_time))
#             sys.exit(0)
#         except Exception as e:
#             pass
#
#
# if __name__ == '__main__':
#     extract()
