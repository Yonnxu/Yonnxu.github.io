def fun(a, b, c):  # a, b,c在函数的定义处，所以是形式参数
    print('a=', a)
    print('b=', b)
    print('c=', c)


# 函数的调秀
fun(10, 20, 30)  # 函数调用时的参数传递，称为位置传参
print('--------------列表的传参  前面加*-----------')
lst = [11, 22, 33]  # 不能直接使用fun(lst)
fun(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入

print('---------------------')
fun(a=100, c=300, b=200)  # 函数的调用，所以是关键字实参
print('--------------字典的传参  前面加**-----------')
dic = {'a': 111, 'b': 222, 'c': 333}
fun(**dic)  # 在函数调用时，将字典中的键值对都转换为关键字实参传入


def fun(a, b=10):  # b是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=', a)
    print('b=', b)


def fun2(*args):  # 个数可变的位置形参
    print(args)


fun2(10, 20, 30)


def fun3(**args2):  # 个数可变的关键字形参
    print(args2)


fun3(a=11, b=22, c=33, d=44, e=55)

'''
若要参数只能使用关键字实参传递(x=n) 只需在前面加上*号
'''


def fun4(a, b, *, c, d):  # 从*之后的参数,在函数调用时,只能采用关键字参数传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# 调用fun4函数
# fun4 (10,20,30,40)#位置实参传递
fun4(a=10, b=20, c=30, d=40)  # 关键字实参传递
fun4(10, 20, c=30, d=40)  # 前两个参数，采用的是位置实参传递，而c, d采用的是关键字实参传递

'''函数定义时的形参的顺序问题'''


def fun5(a, b, *, c, d, **args):
    pass


def fun6(*args, **args2):
    pass


def fun7(a, b=10, *args, **args2):
    pass
