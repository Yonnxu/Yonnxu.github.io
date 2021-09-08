# 1.如何提取单个页面数据
# 2.上线程池，多页面抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", encoding='utf-8',newline='') # newline=''解决换行问题
csvwriter = csv.writer(f)


def download_one_page(url):
    # 页面源码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # trs = table.xpath("./tr")[1:]  # 从第一个开始调用 第0个不要了
    trs = table.xpath("./tr[position()>1]")  # 位置大于1的
    # 拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据做简单的处理: \\ / 去掉
        txt = (item.replace("\\", "").replace("/", "") for item in txt)  # 生成器
        # 把数据存储到文件中
        csvwriter.writerow(txt)
    print(url, "提取完毕")


if __name__ == '__main__':
    # for i in range(1,14870): # 效率极其低
    #   download_one_page(f"http://www.xinfadi.com.cn/marketanalysis/2/list/{i}.shtml")

    # 創建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            # 把下载任务提交给线程池
            t.submit(download_one_page, f"http://www.xinfadi.com.cn/marketanalysis/2/list/{i}.shtml")
    print("下載完成!")
