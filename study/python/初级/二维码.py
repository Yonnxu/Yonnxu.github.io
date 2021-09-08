"""
安装方式:
    pip install MyQR -i https://pypi.tuna.tsinghua.edu.cn/simple
参数说明:
    words (str): 输入文本. !仅支持ASCII字符.
    version (int, 可选): 边长控制. !范围为1 - 40.
    picture (str, 可选): 背景图像. !支持格式{".jpg"，".png"，".bmp"，".gif"}. 默认为黑白色.
    level (str, 可选): 纠错等级. 由低至高{'L','M','Q','H'}. 默认为H.
    colorized (bool, 可选): 使用彩色. 默认不使用.
    save_dir (str, 可选): 存储目录. 默认为程序工作目录.
    save_name (str, 可选): 文件名.
"""
def _run(words, **kwargs):
    from MyQR import myqr
    rst = myqr.run(words, **kwargs)
    print(f"二维码已存储至 {rst[2]}")


def basic(words):
    _run(words, save_name="qrcode_basic.png")


def img_qrcode(words, picture, version=15):
    _run(words,
         picture=picture,
         save_name="qrcode_img.png",
         version=version,
         colorized=True)


def gif_qrcode(words, picture, version=20):
    _run(words,
         picture=picture,
         save_name="qrcode_gif.gif",
         version=version,
         colorized=True)


if __name__ == "__main__":
    # 使用示例
    text = "hello, world"
    # 简单黑白二维码
    # basic(text)
    # 彩色静态二维码
    img_qrcode(text,"3a.png")
    # 彩色动图二维码
    #gif_qrcode(text, "./img/gif_bg.gif")