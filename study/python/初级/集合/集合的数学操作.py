# 1.交集————intersection,&
s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5, 6, 7}
print(s2)
print(s1.intersection(s2))
print(s1 & s2)  # intersection()与&等价,交集操作

# 2.并集操作
print(s1.union(s2))
print(s1 | s2)  # union与 | 等价，并集操作

# 3.差集操作—————difference和-
print(s1.difference(s2))
print(s1 - s2)

# 4.对称差集————symmetric_difference和^
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
