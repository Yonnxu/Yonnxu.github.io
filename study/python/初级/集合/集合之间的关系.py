# 两个集合是否相等（元素相同，就相等）
s = {10, 20, 30, 40, 10}
s2 = {30, 40, 20, 10, 30}
print(s == s2)  # True
print(s != s2)  # False

# 一个集合是否是另一个集合的子集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print('s2是s1的子集', s2.issubset(s1))  # True
print('s3是s1的子集', s3.issubset(s1))  # False

# 一个集合是丕是另―个焦合的 超集(此集合是否包含另一个集合的所以元素)
print('s1是s2的超集？', s1.issuperset(s2))  # True
print('s1是s3的超集', s1.issuperset(s3))  # False

# 两个集合是否含有交集
print('s2和s3是否没有交集？',s2.isdisjoint(s3))  # False
s4 = {100, 200, 300}
print('s2和s4是否没有交集？',s2.isdisjoint(s4))  # True  没有交集为True
