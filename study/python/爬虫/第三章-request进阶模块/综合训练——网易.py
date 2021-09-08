url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data={
"csrf_token": "",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo": "1",
"pageSize": "20",
"rid": "R_SO_4_26830207",
"threadId": "R_SO_4_26830207"
}

# 处理加密过程
e="010001"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
"""
    function a(a) { # 返回16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1) # 循坏16次
            e = Math.random() * b.length, # 随机数
            e = Math.floor(e), # 取整
            c += b.charAt(e); # 取字符串的xxx位置
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) { # 为了让c不产生随机数，设置下面的函数的i为常量
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d:数据 e:010001 f:很长 g:"0CoJUm6Qyw8W8jud"
        var h = {}
          , i = a(16); # i是一个16位的随机值
        return h.encText = b(d, g),
        h.encText = b(h.encText, i), # 返回的是params
        h.encSecKey = c(i, e, f), # 得到的是encSecKey，e和f是死的，
        h
    }
"""