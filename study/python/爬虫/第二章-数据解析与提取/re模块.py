import re

#
# # findall:匹配字符串中所有的符合正则的内容
# lst = re.findall(r"\d+","我的电话号是:10086，我女朋友的电话是:10010")
# print(lst)
#
# # finditer:匹配字符串中所有的内容[返回的是迭代器]
# it = re.finditer(r"\d+","我的电话号是:10086，我女朋友的电话是:10010")
# for i in it:
#     print(i.group()+' finditer')
#
# # search找到一个结果就返回，可以用来判断是否存在，
# # search返回的结果是match对象，拿数据需要.group()
# s = re.search(r"\d+","我的电话号是:10087，我女朋友的电话是:10010")
# print(s.group())
#
# # match默认从头开始匹配，其他的是全局，如果头部没有就为空值
# s1= re.match(r"\d+","10088，我女朋友的电话是:10010")
# print(s1.group())
#
# # 预加载正则表达式
# obj=re.compile(r"\d+")
# ret=obj.finditer('我的电话号是:10017，我女朋友的电话是:10011')
# for it in ret:
#     print(it.group())
#
# rer=obj.search('我的电话号是:11087，我女朋友的电话是:10010')
# print(rer.group())

s = '''
<div class='gql'><span id='1'>郭麒麟</span></div>
<div class='jay'><span id='2'>周杰伦</span></div>
<div class='mzx'><span id='3'>没自信</span></div>
<div class='go'><span id='4'>去</span></div>
'''

# (?P<name>.*?)————.*? 匹配到的内容会赋给<>里面的name属性
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)  # re.S:可以让.能匹配换行符避免断层
result=obj.finditer(s)
for it in result:
    print(it.group('id')+'  '+it.group('name'))