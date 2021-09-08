# 拿到页面源码. requests
# 通过re获取想要的有效信息
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
resp = requests.get(url,headers=headers)
page_content=resp.text
# 解析数据
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<num>.*?)</span>.*?<span>(?P<people>.*?)</span>',re.S)
# 开始匹配
result=obj.finditer(page_content)
f=open("data.csv",mode="w")
csvwriter=csv.writer(f)
for it in result:
    # print('名字:'+it.group('name')+'  年份:'+it.group('year').strip()+'  评分:'+it.group('num')+'  评价:'+it.group('people'))
    dic = it.groupdict()
    dic['year']=dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()