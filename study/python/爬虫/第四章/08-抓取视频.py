# 用户上传视频 ->转码(把视频做处理，2k，1080，标清) -> 切片处理（把单个文件拆分）
# 用户在拉动进度条时，只加载进度条后面的几个切片，前面的不加载
# =============================

# 需要一个文件记录：1.视频播放顺序，2.视频存放的路径
# M3U8 txt json =>文本

# 想要抓取一个视频：
# 1.找到M3U8（各种手段）
# 2.通过M3U8下载到ts文件
# 3.通过各种手段（不仅仅是编程手段） 把ts文件合并为一个mp4文件

# 流程:
# 1．拿到html的页面源代码
# 2．从源代码中提取到m3u8的url
# 3．下载m3u8
# 4．读取m3u8文件,下载视频5．合并视频


import requests
import re
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# # 不能用Xpath，因为这个是js的代码不是HTML
# obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取M3U8的地址
#
# url = "https://www.91kanju.com/vod-play/57218-2-2.html"
# resp = requests.get(url,headers=headers)
# # print(resp.text)
# m3u8_url = obj.search(resp.text).group("url")  # 拿到地址
# resp.close()
# # 下载m3u8文件
# resp2=requests.get(m3u8_url,headers=headers)
# with open("窥探.m3u8",mode="wb") as f:
#     f.write(resp2.content)
#
# resp2.close()


# 解析m3u8文件
n=1
with open("窥探.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line=line.strip() # 去掉空白，空格，换行符
        if line.startswith("#"): #如果以#开头就不要
            continue
        # print(line)
        # 下载视频的片段

        resp3=requests.get(line)
        f=open(f"video/{n}.ts",mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1
        print("完成1了个")