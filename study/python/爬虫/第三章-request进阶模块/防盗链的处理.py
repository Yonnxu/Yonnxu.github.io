# 1.拿到contId
# 2.拿到videoStatusUrl返回的JSON 返回一个srcURL
# 3.srcURL里面的内容进行修整
# 4.下载视频
import requests

url = "https://www.pearvideo.com/video_1735229"
contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.2235608532929787"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    # 防盗链：溯源——当前本次请求的上一级是谁 即url
    "Referer": url
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systeamTime = dic['systemTime']
srcUrl=srcUrl.replace(systeamTime,f'cont-{contId}')

# 下载视频
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)

print("OK")