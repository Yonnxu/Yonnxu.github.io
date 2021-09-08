sorce = float(input('请输入成绩'))

if sorce > 100:
    print('成绩录入错误')
elif sorce >= 90:
    print('A')
elif sorce >= 80:
    print('B')
elif sorce >= 70:
    print('C')
elif sorce >= 60:
    print('D')
elif sorce >= 0:
    print('E')
else:
    print('成绩录入错误')

