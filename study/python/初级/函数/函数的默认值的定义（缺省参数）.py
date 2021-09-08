def fun(a, b=10):  # b称为默认值参数
    print(a, b)


# 函数的调用
fun(100)
fun(20, 30)

print('hello', end='\t')  # end 的默认值是 \n————换行
print('world')
# 一般缺省参数要放在函数调用的末尾