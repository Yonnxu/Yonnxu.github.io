scores = {'张三': 100, '李四': 98, '王五': 45}
print('---------------获取key值---------------')
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的key组成的视图转成列表

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))  # 将所有的value组成的视图转成列表

# 获取所有的key-value对
items = scores.items()
print(items)
print(list(items))  # 转换后的列表元素是由元祖组成
