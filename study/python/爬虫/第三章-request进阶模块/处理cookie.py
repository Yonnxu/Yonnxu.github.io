import requests

# 会话
# session = requests.session()
# data = {
#     "loginName": "Administrator_AD",
#     "password": "141200.kid"
# }
# 1.登录
# url = "https://passport.17k.com/ck/user/login"
# session.post(url, data=data)
# 2.拿数据
# 刚才的session会话中有cookie 使用request会再重新请求一个
# resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')

# 4-14行可以不用session用下面方法替代
resp = requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919', headers={
    "Cookie": "GUID=ccee28fd-ad4d-4d37-8aa8-86bd25d2f7cb; c_channel=0; c_csc=web; BAIDU_SSP_lcr=https://graph.qq.com/; Hm_lvt_9793f42b498361373512340937deb2a0=1626192341,1626239107,1626239116,1626239137; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F14%252F54%252F82%252F78158254.jpg-88x88%253Fv%253D1626241343000%26id%3D78158254%26nickname%3DAdministrator_AD%26e%3D1641793466%26s%3D34b75de4ca40a74e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2278158254%22%2C%22%24device_id%22%3A%2217a9e411af371-023c87c480fb94-6373264-2073600-17a9e411af7225%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22ccee28fd-ad4d-4d37-8aa8-86bd25d2f7cb%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1626244101"
})
print(resp.text)
