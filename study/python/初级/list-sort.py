lst = [20, 10, 5, 1, 100]
print('排序前:', lst, id(lst))

# 开始排序,调用列表对象的sort方法,升序排序
lst.sort()
print('排序后:', lst, id(lst))

# 通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)  # reverse=True表示降序排序，reverse=False就是升序排序
print(lst)

print('-----------使用内置函数sorted()对列表进行排序,将产生一个新的列表---------------')
lst = [20, 10, 5, 1, 100]
print(lst, id(lst))
# 开始排序
new_list=sorted(lst)
print(lst)
print(new_list)
# 降序排序
desc_list=sorted(lst,reverse=True)
print(desc_list,id(desc_list))