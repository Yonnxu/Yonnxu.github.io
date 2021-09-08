# 线程池: 一次性开辟一些线程,用户直接给线程池提交任务,线程任务的调度给线程池完成
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(100):
        print(name, i)


if __name__ == '__main__':
    # # 创建一个有50个线程组成的线程池
    # with ThreadPoolExecutor(50) as t:
    #     for i in range(100):
    #         t.submit(fn, name=f"线程{i}")
    # # 等待线程池中的任务执行完毕 才会执行(守护)
    # print('123')

    # 创建进程池
    with ProcessPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")
    # 等待进程池中的任务执行完毕 才会执行(守护)
    print('123')
