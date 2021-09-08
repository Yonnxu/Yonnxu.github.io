# lst = [{'rating': [9.7, 20682397], ' id': '1292052', 'type': ['犯罪', '剧情'], 'title': '肖申克的救赎',
#         'actors': ['蒂姆·罗宾斯', '摩根·弗里曼']},
#        {'rating': [9.6, 1528760], 'id': '1291546', 'trpe': ['剧情', '爱情', '同性'], 'title': '霸王别姬',
#         'actors': ['张国荣', '张丰毅', '巩俐', '葛优']},
#        {'rating': [9.5, 1559181], 'id': '1292720', 'type': ['"剧情', '爱情'], ' title': '阿甘正传',
#         'actors': ['汤姆·汉克斯', '罗宾·怀特']}
#        ]
# name = input('输入要查询的演员')
# for item in lst:  # 遍历列表  -->{} item是一个有一个的字典
#     act_lst = item['actors']
#     if name in act_lst:
#         print(name+' 出演了 '+item['title'])


# 如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
# finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
except ZeroDivisionError:
    print('沙雕吗？')
except ValueError:
    print('该输入无法转化为数字')
else:
    print('结果为', result)
finally:
    print('管你出不出问题，运行就完事了')

# 1.除(或取模)零(所有数据类型)
# print (10/0)  # ZeroDivisionError

# 2.序列中没有此索引(index)
lst = [11, 22, 33, 44]
# print(lst[4]) #IndexError   索引从0开始

# 3.映射中没有这个键
dic = {'name': '张三', 'age': 20}
# print(dic['gender']) #KeyError

# 4.未声明/初始化对象（没有属性)
# print (num) #NameError

# 5.Python语法错误
# int a=20 #SyntaxError

# 6.传入无效的参数
# a = int('hello')  # ValueError
