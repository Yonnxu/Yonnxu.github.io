scores = {'张三': 100, '李四': 98, '王五': 45}
print('第一种方式，使用[]', scores['张三'])
# print(scores['陈六’])#KeyError: ‘陈六’
print('第二种方式，使用get()方法', scores.get('张三'))
print(scores.get('陈六'))  # None
print(scores.get('麻七', 99),'若键值不存在则输出默认值99')
