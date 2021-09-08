# import time
#
#
# def func():
#     print('1')
#     time.sleep(1)  # 让当前线程处于阻塞状态，CPU不会为这个线程工作
#     print('2')
#
#
# if __name__ == '__main__':
#     func()
# input()也是处于阻塞状态
# requests.get(bilibili) 在服务器返回数据前，也是处于阻塞状态
# 一般情况下，当程序处于IO操作（input，output）的时候，线程都会处于阻塞状态

# 协程：当程序遇到IO操作时，可以选择性的切换到其他任务上。
# 在微观上是一个任务一个任务的进行切换．切换条件一般就是IO操作
# 在宏观上,我们能看到的其实是多个任务一起在执行
# 多任务异步操作

# 上方所讲的一切.都是在单线程的条件下
#
import asyncio
#
#
#
# # python编写协程的程序
#
# async def func():
#     print('11')
#
# if __name__ == '__main__':
#     g=func() # 此时的函数是异步协程函数，函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g) # 协程程序运行需要asyncio模块的支持

#
# import time
#
# async def func1():
#     print('22')
#     # time.sleep(3) # 当程序出现了同步操作时，异步中断
#     await asyncio.sleep(3) # 异步操作的代码
#     print('33')
#
#
# async def func2():
#     print('44')
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print('55')
#
#
# async def func3():
#     print('66')
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print('77')
#
#
# if __name__ == '__main__':
#     f1=func1()
#     f2=func2()
#     f3=func3()
#     tasks=[
#         f1,f2,f3
#     ]
#     t1=time.time()
#     # 一次性启动多个任务(协程)
#     asyncio.run(asyncio.wait(tasks))
#     t2=time.time()
#     print(t2-t1)


import time


async def func1():
    print('22')
    await asyncio.sleep(3)  # 异步操作的代码
    print('33')


async def func2():
    print('44')
    await asyncio.sleep(2)
    print('55')


async def func3():
    print('66')
    await asyncio.sleep(4)
    print('77')


async def main():
    # 第一种写法
    # f1=func1()
    # await f1 # 一般await挂起操作放协程对象前面

    # 第二种写法
    tasks = [
        asyncio.create_task(func1()),  # 在py3.8以后加上asyncio.create_task()
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    # 一次性启动多个任务(协程)
    asyncio.run(main())

    t2 = time.time()
    print(t2 - t1)

# # 爬虫的应用
# async def download(url):
#     print('正在下载')
#     await asyncio.sleep(2) # 网络请求
#     print('下载完成')
#
# async def main():
#     urls=[
#         "http://www.baidu.com",
#         "http://www.bilibili.com",
#         "http://www.163.com"
#     ]
#     tasks=[]
#     for url in urls:
#         d=download(url)
#         tasks.append(d)
#
#     await asyncio.wait(tasks)
# if __name__ == '__main__':
#     asyncio.run(main())
