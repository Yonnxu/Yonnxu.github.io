a = 10
b = 10
print(a == b)  # True说明，a与b的value 相等
print(a is b)  # True说明, a与b的id标识,相等

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # value-->True
print(lst1 is lst2)  # id -->False  两个数组不能用同一个地址 否则改一个数组时另一个数组也跟着变

print(a is not b)  # False a和b的地址不相等吗
print(lst1 is not lst2)  # True
