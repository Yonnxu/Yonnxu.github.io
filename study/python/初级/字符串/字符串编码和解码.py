s = '立于浮华之世'
# 编码
print(s.encode(encoding='GBK'))  # 在GBK这种编码格式中 一个中文占2个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编辑格式中,一个中文占3个字节

# 解码
# bytes代表一个二进制数据（字节类型数据）
byte=s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码

byte=s.encode(encoding='UTF-8')  # 编码
print(byte.decode(encoding='UTF-8'))  # 解码
