from multiprocessing import Process
import time
from threading import Thread

def func():
    for i in range(100):
        print('子进程', i)
        time.sleep(0.1)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()

    for i in range(100):
        print('主进程', i)
        time.sleep(0.1)




# 给线程传递参数
# def func(name):
#     for i in range(100):
#         print(name, i)
#         # time.sleep(0.1)
#
#
# if __name__ == '__main__':
#     p1 = Thread(target=func,args=("周杰伦",)) # 传递参数必须是元组
#     p1.start()
#
#     p2 = Thread(target=func,args=("王力宏",))
#     p2.start()