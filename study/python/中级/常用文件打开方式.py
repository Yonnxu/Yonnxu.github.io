# r    以只读模式打开文件，文件的指针将会放在文件的开头
# w    以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
# a    以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾
# b    以二进制方式打开文件，不能单独使用，需要与共它模式一起使用，rb，或者wb
# +    以读写方式打开文件，不能单独使用，需要与其它模式一起使用，a+


file = open('b.txt', 'w')
file.write('Python')
file.close()

file = open('c.txt', 'a')
file.write('Python')
file.close()

src_file = open('111.png', 'rb')
target_file = open(' copylogo. png', 'wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()

'''
上面的图片复制相当于
with open('111.png，rb')as src_file:
    with open('copy21ogo. png', 'wb')as target_file:
        target_file.write(src_file.read())
        不需要开启和关闭的过程
'''
