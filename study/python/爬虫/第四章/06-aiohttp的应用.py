import asyncio
import aiohttp

urls = [
    "http://i1.shaodiyejin.com/uploads/tu/201704/9999/7a396d84a5.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201704/9999/504b5d1f65.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201704/9999/e335845a3a.jpg"
]


async def download(url):
    # 从右边切一次，取第2个的位置 ————http://i1.shaodiyejin.com/uploads/tu/201704/9999是[0],7a396d84a5.jpg是[1]
    name = url.rsplit("/", 1)[1]
    # with可以自动关闭session服务
    async with aiohttp.ClientSession() as session: # requests
        async with session.get(url) as resp: # resp=requests.get()
            # 请求回来了，写入文件
            with open(f"images/{name}", mode="wb") as f: # 创建文件
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
    print(name,"OK")

    # s=aiohttp.ClientSession()  <==> requests
    # 发送请求，
    # 得到图片
    # 内容写入


async def main():
    tasks = []
    for url in urls:
        tasks.append(download(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
