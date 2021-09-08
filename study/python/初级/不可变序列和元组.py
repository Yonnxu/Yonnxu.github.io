print('-----------------可变序列  列表 字典   有增删改的操作 内存地址不会发生改变----------------')
lst = [1, 2, 3, 4, 5]
print(lst, id(lst))
lst.append(3000)
print(lst, id(lst))

print('----------------不可变序列 字符串，元组  没有增删改的操作 内存地址会发生改变------------')
str = 'hello'
print(str, id(str))
str = str + 'world'
print(str, id(str))

print('====================元组的创建======================')
t = ('hello', 'world', 88)
print('1.使用()创建元组', t, type(t))

t2 = 'hello', 'world', 88
print('2.省略()创建元组', t2, type(t2))

t1 = tuple(('hello', 'world', 88))
print('3.使用内置函数tuple()创建元组', t1, type(t1))

t3 = ('python',)
print('4.如果元组中占有一个元素，那么逗号不能省略---------', t3, type(t3))

t4 = ()
t5 = tuple()
print('4.空元组的创建方式---------', t4, type(t4), t5, type(t5))

lst={}
print('4.空字典的创建方式---------',lst, type(lst))