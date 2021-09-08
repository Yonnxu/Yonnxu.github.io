from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

# 准备好参数配置
opt=Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")
web = Chrome(options=opt) # 把参数配置设置到浏览器

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

time.sleep(2)
# # 定位到下拉列表
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# # 对元素进行包装，包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器进行调整选项
# # <select>
# #     <option value="1">哈哈</option>
# #     <option value="2">阿巴</option>
# # </select>
# # select_by_index()————根据当前的位置切换 1
# # select_by_value()————根据value的值切换 1,2
# # select_by_visible_text()————根据文本内容切换 哈哈，阿巴
# for i in range(len(sel.options)):  # i是每一个下拉框选项的索引位置
#     sel.select_by_index(i)  # 按照索引切换
#     time.sleep(2)
#     table=web.find_element_by_xpath('//*[@id="TableList"]/table')
#     print(table.text) # 打印所有的文本
#     print("============")
# print('完毕')
# web.close()

# 如何拿到页面代码Elements(经过数据加载以及js执行之后的结果的html内容)
print(web.page_source)
