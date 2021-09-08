# 原理：通过第三方机器发送请求
import requests

# 站大爷——106.45.104.218:3266
proxies={
    "https":"https://106.45.104.218:3266"
}

resp = requests.get("http://www.baidu.com",proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
