for i in range(1, 4):  # 执行三次 一次是一行
    for j in range(1, 5):
        print('★', end='\t')  # 不换行输出
    print()  # 打行

for i in range(1, 10):
    for j in range(1, 1 + i):
        print('☆', end='')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i , '*' , j , '=' , i * j , end='   ')
    print()
