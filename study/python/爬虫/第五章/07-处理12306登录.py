from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from chaojiying import Chaojiying_Client
import time

# 初始化超级鹰
chaojiying = Chaojiying_Client('2195249372', '141200.kid', '919980')

# 如果程序被识别到是自动的怎么办
# 1.谷歌版本小于88: 启动浏览器时(此时没有加载任何网页内容),向页面嵌入js代码,去掉识别的webdriver
# web = Chrome()
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#     navigator.webdriver = undefined
#     Object.defineProperty(navigator，'webdriver', {
#         get: () =>undefined
#     })
# """
# })
# web.get(xxxxxXx)

# 2.谷歌版本大于88
option=Options()
# option.add_experimental_option('excludeSwitches'，['enable-automation']
option.add_argument('--disable-blink-features=AutomationControlled')



web = Chrome(options=option)

web.get('https://kyfw.12306.cn/otn/resources/login.html')

time.sleep(2)
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(5)

# 处理验证码
verify_img_elment = web.find_element_by_xpath('//*[@id="J-loginImg"]')

# 用超级鹰识别验证码
dic = chaojiying.PostPic(verify_img_elment.screenshot_as_png, 9004)
result = dic['pic_str']  # 返回坐标 x1,y1|x2,y2|x3,y3|...
rs_list = result.split("|")
for rs in rs_list:  # x1,y1
    p_temp = rs.split(",")
    x = int(p_temp[0])
    y = int(p_temp[1])
    print(x,y)
    # 让鼠标移动到某一个位置，然后点击
    # 移动到节点，然后按当前节点的坐标的偏移量移动
    ActionChains(web).move_to_element_with_offset(verify_img_elment, x, y).click().perform()  # perform()提交

time.sleep(5)
# 输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("123456789")
web.find_element_by_xpath('//*[@id="J-password"]').send_keys("123456789")
web.find_element_by_xpath('//*[@id="J-login"]').click()

btn=web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(btn).drag_and_drop_by_offset(btn,300,0).perform() # 抓起来 拉到哪