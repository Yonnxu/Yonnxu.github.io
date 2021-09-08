def fac(n):
    if n == 1:
        return 1
        print(n)
    else:
        return n * fac(n - 1)
        print(n)


print(fac(6))


def sum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sum(n - 2) + sum(n - 1)


# 斐波那契数列第6位上的数字
print(sum(6))

print(' -----------------')
# 输出这个数列的前6位上的数字
for i in range(1, 7):
    print(sum(i))