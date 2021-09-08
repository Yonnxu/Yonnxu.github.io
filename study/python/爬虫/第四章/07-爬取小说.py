from lxml import etree
import requests
import csv
import time

headers = {
    "cookie": "Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902=1626602886; PHPSESSID=4j5c2r9fek2k2jsrdb8gpshnu3pa84f4; jieqiUserInfo=jieqiUserId%3D428787%2CjieqiUserName%3D2195249372%2CjieqiUserGroup%3D3%2CjieqiUserVip%3D0%2CjieqiUserName_un%3D2195249372%2CjieqiUserHonor_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1626602906; jieqiVisitInfo=jieqiUserLogin%3D1626602906%2CjieqiUserId%3D428787; jieqiVisitId=article_articleviews%3D2017; Hm_lvt_acfbfe93830e0272a88e1cc73d4d6d0f=1626602939; Hm_lpvt_acfbfe93830e0272a88e1cc73d4d6d0f=1626602939; Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902=1626603667",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",

}
url = "https://www.wenku8.net/novel/0/1/index.htm"
resp = requests.get(url, headers=headers)
resp.encoding = 'gbk'
# 保存地址
myUrl = []
# 解析HTML文档对象
html = etree.HTML(resp.text)
tables = html.xpath("/html/body/table/tr/td/a/@href")[1:]
# 设置存储名字
text = html.xpath("/html/body/table/tr/td/a/text()")
resp.close()
for id in tables:
    # 获取头部的url
    fsturl=url.rsplit('/',1)[0]
    # 拼接
    urls = f"{fsturl}/{id}"
    # print(urls)
    myUrl.append(urls)
i = 0
for url in myUrl:
    res = requests.get(url, headers=headers)
    res.encoding = 'gbk'
    # print(res.text)
    divs = etree.HTML(res.text)
    div = divs.xpath('.//*[@id="content"]')
    # print(res.text)
    for a in div:
        # print(url)
        txt = a.xpath("./text()")
        # 把数据存储到文件中
        txt = (item for item in txt)  # 生成器
        with open(f"novel/{text[i]}", mode="w",encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(txt)

        print(url+" 下载完成")
    i = i + 1
    res.close()
    # 休眠：防止认为是恶意攻击
    time.sleep(10)
print("全部完成")
