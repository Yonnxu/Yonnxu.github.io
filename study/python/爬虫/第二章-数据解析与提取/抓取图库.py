# 1.拿到主页面源码，提取到子页面的链接地址，href
# 2.通过href拿到子页面内容，从子页面找到下载地址
# 3.下载图片
import requests
from bs4 import BeautifulSoup
import time
url='https://www.umei.net/katongdongman/dongmantupian'
resp = requests.get(url,stream=True)
resp.encoding='utf-8' # 处理乱码
# print(resp.text)

# # 把源码给bs
main_page = BeautifulSoup(resp.text, "html.parser")
# print(main_page)
alist = main_page.find("div", class_="TypeList").find_all("a")
for a in alist:
    href="https://www.umei.net"+a.get('href') # 直接通过get就可以获取
    # 拿到子页面的源码
    child_page_resp=requests.get(href,stream=True)
    child_page_resp.encoding='utf-8'
    child_page_text=child_page_resp.text
    # 从子页面拿到图片下载路径
    child_page=BeautifulSoup(child_page_text,"html.parser")
    p=child_page.find("p",align="center")
    img=p.find("img")
    src=img.get("src")

    # 下载图片
    img_resp=requests.get(src)
    img_name=src.split('/')[-1] # 拿到url中最后一个/以后的内容
    with open("img/"+img_name,mode="wb") as f:
        # 字节内容写入文件
        f.write(img_resp.content)     # img_resp.content---拿到字节
    print('over',img_name)
    time.sleep(1)
print("all over!!!")