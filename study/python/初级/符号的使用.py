# 将数据输出文件中
# 注意点:
# 1，所指定的盘符在存在
# 2.使用file= fp
# fp=open('D:/text.txt','a+') #如果文件不存在就创建,存在就在文件内容的后面继续追加
# print('helloworld',file=fp)
# fp.close()
print('hello\rwor')  # \r 覆盖前面的内容
print('hello\nworld')  # \n 换行
print('hello\bworld')  # \b 退一个格
print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')
# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
print(r'hello\nworld')
# 注意事项，最后一个字符不能是反斜杠
# print (r'hello \nworld\ ')
print(r'hello\nworld\\')
