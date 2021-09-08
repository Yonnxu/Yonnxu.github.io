# 向列表末尾添加一个元素
lst = [1, 2, 3, 4, 5]
print('添加元素之前', lst, id(lst))
lst.append(100)
print('append添加元素之后', lst, id(lst))

# 向列表末尾添加至少一个元素
lst2 = ['hello', 'world']
lst.append(lst2)  # 将lst2做为一个元素添加到列表的末尾
print('append添加列表之后', lst, id(lst))
# 向列表的末尾一次性添加多个元素
lst.extend(lst2)
print('extend添加列表之后', lst, id(lst))

# 在任意位置上添加一个元素
lst.insert(1, 9)
print('insert添加元素之后', lst, id(lst))

lst3 = [True, False, 'mmd']

# 在任意位置添加n个元素
lst[100:] = lst3
print('使用切片替换到100的元素之后', lst, id(lst))

print('-------------------------列表元素的删除-------------------------')
demo = [1, 2, 3, 4, 5, 6, 7, 8]
demo.remove(2)  # 移除2这个元素而不是位置 根据元素移除
print('使用remove删除列表元素为2的这个元素', demo)  # 从列表中移除一个元素，如果有重复元素只移第一个元素

# pop(根据索引移除元素
demo.pop(1)  # 移除第1+i个元素 根据位置移除
print('使用pop删除第i+1个元素位置的元素', demo)

demo.pop()  # 如果不指定参数 则删除列表中最后一个元素
print('使用pop的空对象方法删除列表中的最后一个元素', demo)

new_demo = demo[1:3]  # 只保留demo列表中1,2两个位置的元素
print('原列表', demo)
print('切片后的新列表', new_demo)

demo[1:3] = []
print('把demo列表中处在1,2位置的元素使用空列表进行替代', demo)

demo.clear()
print('使用clear删除列表中所以元素', demo)

del demo
print('使用del删除列表')
# print(demo) # NameError: name 'demo' is not defined


print('-----------------列表的修改---------------------')
lis = [10, 20, 30, 40, 50]
print(lis,id(lis))
lis[2] = 100
print('修改lis列表的第1+i个位置的元素', lis)

lis[1:3] = [300, 400, 500, 600]
print("使用切片替换位于1,2位置的元素", lis,id(lis))
