import requests
from lxml import etree

url = "https://shaoyang.zbj.com/search/f/?type=new&kw=css"
resp = requests.get(url)

# 解析
html = etree.HTML(resp.text)

# 拿到每个服务商的div
divs = html.xpath ("/html/body/div[6]/div/div/div[2]/div[5]/div/div")

for div in divs:  # 每一个服务商信息
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = "sass".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[1].replace("\n", "")
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")
    print(com_name)
