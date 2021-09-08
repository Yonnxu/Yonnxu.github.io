# 1.拿到源代码
# bs4解析，拿到数据
import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml'
resp = requests.get(url)

f=open("菜价.csv",mode='w',encoding='utf-8')
csvwriter=csv.writer(f)
# print(resp.text)

# 解析数据
# 1.把页面源码给BeautifulSoup处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析
# 2.从bs对象中查找数据
# find(标签，属性=值) 找到一个就返回
# find_all(标签，属性=值) 全局查找
# page.find("table",class_="hq_table") # class是Python的关键字 _可以避免class
table = page.find("table", attrs={"class": "hq_table"})  # 和上一行一个意思，可以避免class
# 拿到所有的数据行
trs = table.find_all("tr")[1:]  # 先找到所有的数据，然后做切片，从第1个开始切，(第0个被切没了)
for tr in trs:  # 每一行
    tds = tr.find_all("td")  # 每行中的所有td
    name = tds[0].text  # .text表示拿到被标签标记的内容
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    date = tds[6].text
    csvwriter.writerow([name,low,avg,high,gui,kind,date])
f.close()
print('over')