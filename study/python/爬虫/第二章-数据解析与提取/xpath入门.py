# xpath 是在XML文档中搜索内容的一门语言
# html是xml的一个子集
from lxml import etree
parser = etree.HTMLParser(encoding="utf-8") # 默认是xml解析，需要自己创建解析器
tree = etree.parse("b.html",parser=parser)  # 把xml中的内容给tree这个对象
# result=tree.xpath('/html')
# result = tree.xpath("/html/body/ul/li[1]/a/text()")  # xpath的順序是从1开始
# result = tree.xpath("/html/body/ul/li/a[@href='tachiba']/text()")  # [@xxx=xxx] 属性名的筛选
# print(result)

ol_li_list=tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    # 从每个li中提取到文件信息    ./————当前节点
    result = li.xpath("./a/text()") # 在li中查找,相对查找
    print(result)

    # 获取属性的名称
    result2 = li.xpath("./a/@href")
    print(result2)

print(tree.xpath("/html/body/ul/li/a/@href"))