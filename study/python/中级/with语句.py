# 为什么使用with语句:如果程序在打开文件的途中有错误 那么最后的close语句则执行不了 虽然可以把close（）放到finally中去处理 但是太麻烦 这时可以使用with语句来处理

class MyContentMgr(object):
    def __enter__(self):
        print(' enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print(' show方法被调用执行了')



with MyContentMgr() as file:   #相当于file=MyContentMgr ( )
    file.show()

'''
1.当with语句执行时，便执行上下文表达式（context_expr）(一般为某个方法)来获得一个上下文管理器对象，
上下文管理器的职责是提供一个上下文对象，用于在with语句块中处理细节：

2.一旦获得了上下文对象，就会调用它的__enter__()方法，将完成with语句块执行前的所有准备工作，如果with语句后面跟了as语句，
则用__enter__()方法的返回值来赋值；

3.当with语句块结束时，无论是正常结束，还是由于异常，都会调用上下文对象的__exit__()方法，__exit__()方法有3个参数，
如果with语句正常结束，三个参数全部都是 None；
如果发生异常，三个参数的值分别等于调用sys.exc_info()函数返回的三个值：类型（异常类）、值（异常实例）和跟踪记录（traceback），相应的跟踪记录对象。

4.因为上下文管理器主要作用于共享资源，__enter__()和__exit__()方法基本是完成的是分配和释放资源的低层次工作，
比如：数据库连接、锁分配、信号量加/减、状态管理、文件打开/关闭、异常处理等。
'''