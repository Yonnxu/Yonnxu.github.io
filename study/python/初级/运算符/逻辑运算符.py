# 布尔运算符
a, b = 1, 2
print('------------and 并且---------------')
print(a == 1 and b == 2)  # True    True and True-->True
print(a == 1 and b < 2)  # False    True and False -->False
print(a != 1 and b == 2)  # False    False and True-->False
print(a != 1 and b != 2)  # False    False and False -->False

print('----------------or或者----------------------')
print(a == 1 or b == 2)  # True or True -->True
print(a == 1 or b < 2)  # True or False -->True
print(a != 1 or b == 2)  # False or True -->True
print(a != 1 or b != 2)  # False or False -->False

print('------------not 对bool类型操作数取反----------')
f = True
f2 = False
print(not f)
print(not f2)

print('------------in 与not in------------------------------')
s = 'helloworld'
print('w' in s)  # True    w是否在s中存在
print('k' in s)
print('w' not in s)  # False  w是否在s中不存在
print('k' not in s)  # True

print('---------运算符优先级: 先 and  后 or  最后 =  -----------')