# 每一个进程至少要有一个线程
# 线程是执行单位
# 启动每一个程序默认会有一个主线程

# def func():
#     for i in range(100):
#         print("func",i)
#
# if __name__=='__main__':
#     func()
#     for i in range(100):
#         print("func", i)

# 多线程
from threading import Thread  # 线程类


#
#
# def func():
#     for i in range(100):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     t=Thread(target=func) # 创建一个线程，给func安排任务
#     t.start() # 开始执行该线程 只是给一个状态，具体执行时间由CPU决定
#     for i in range(100):
#         print("main", i)

class MyThread(Thread):
    def run(self):  # run是固定的  ->当线程被执行的时候，被执行的就是run()
        for i in range(100):
            print("子线程", i)


if __name__ == '__main__':
    t = MyThread()
    # t.run()  # 方法的调用
    t.start()  # 开启线程
    for i in range(100):
        print("主线程", i)
