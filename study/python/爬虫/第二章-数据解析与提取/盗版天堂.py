# 1.定位片
# 2.提取子页面链接地址
# 3.请求子页面链接地址，拿到下载地址
import re
import requests

domain="https://www.dy2018.com/"

# resp=requests.get(domain,verify=False)# verify=False去掉安全验证
resp = requests.get(domain)
resp.encoding='gb2312' # 指定字符集

# 拿到ul里面的li
obj1=re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3=re.compile(r'◎片　　名(?P<movie>.*?)<.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

result1=obj1.finditer(resp.text)
child_href_list=[]
for it in result1:
    ul=it.group('ul')
    # 提取子页面链接
    result2=obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面的url地址
        child_href=domain + itt.group('href').strip("/")
        child_href_list.append(child_href) # 把子页面链接保存起来


# 提取子页面地址
for href in child_href_list:
    child_resp=requests.get(href)
    child_resp.encoding='gbk'
    result3= obj3.search(child_resp.text)
    print(result3.group('movie')+'    '+result3.group('download'))