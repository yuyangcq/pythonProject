from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
# 打开浏览器
url = 'http://bond.sse.com.cn/bridge/information/index_detail.shtml?bound_id=13994' 
browser = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
browser.get(url)
'''
WebDriverWait：等待指定元素加载完毕后，再继续执行后续代码。
implicitly_wait：针对页面，对所有元素设置超时时长。
sleep：强制等待，不管画面加载是否完成，都会休眠固定时长。
'''
time.sleep(0.5)
# element = WebDriverWait(browser, 1上海证券交易所.py0).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "align_left"))
# )
# 提取页面元素
print('债券名称：' + browser.find_element_by_xpath('//*[@id="AUDIT_NAME"]').text)
print('项目状态：' + browser.find_element_by_xpath('//*[@id="AUDIT_STATUS"]').text)
print('更新日期：' + browser.find_element_by_xpath('//*[@id="PUBLISH_DATE"]').text)
# 退出浏览器 
browser.quit()