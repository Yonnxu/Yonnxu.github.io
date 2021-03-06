from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()
web.get("https://www.chaojiying.com/user/login/")

# 處理图片 screenshot_as_png————截屏以png格式保存
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('2195249372', '141200.kid', '919980')
dic=chaojiying.PostPic(img, 1902)
verify_code=dic['pic_str']

# 向页面填写用户名，密码，验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("2195249372")
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("141200.kid")
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(10)
# 点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()