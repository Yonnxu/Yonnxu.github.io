# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

import requests
query=input('输入要查询的人物')
url = f'https://www.sogou.com/web?query={query}'

# 修改headers的值伪装成网页访问
dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
resp = requests.get(url, headers=dic)  # 处理反爬
print(resp)
print(resp.text)
resp.close()