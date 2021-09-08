from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("http://lagou.com")

# 找到某个元素，点击它
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a/i')
el.click()  # 点击事件

time.sleep(1)  # 防止网页未加载出来就执行输入操作从而找不到报错

# 找到输入框输入Python=>输入回车/点击搜索
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

# 查找存放数据的位置，进行数据提取
# 找到页面中存放数据的所有的li
li_list=web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name=li.find_element_by_tag_name("h3").text
    job_price=li.find_element_by_xpath("./div/div/div[2]/div/span").text
    company_name=li.find_element_by_xpath('./div/div[2]/div/a').text
    print(job_name,job_price,company_name)
web.close()