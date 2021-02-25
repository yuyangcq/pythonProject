from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
import re
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests,lxml.etree
import urllib.parse
import urllib.request
from string import digits
import time
import datetime


if __name__ == '__main__':


   while(True):
        headers={
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
           "Cookie":"__guid=128030490.2831871680830658600.1597218666700.9712; monitor_count=27"
        }
        proxies = {
           "https":"https://171.35.171.227:9999",
           "http":"http://171.35.171.227:9999"
        }
        count = 1
        downLoadImageUrl = "https://human.amac.org.cn/gs/photo/160013006027816001300602780.jpg"
        print(downLoadImageUrl)
        localPath  = "F:\\图片\\"
        isExists=os.path.exists(localPath)
        if not isExists:
            os.makedirs(localPath)
        # user_name_result = check(userName,count)
        response = requests.get(url=downLoadImageUrl, headers=headers,verify=False,timeout=5)
        with open(localPath+str(int(time.time() * 1000))+".jpg", 'wb') as fr:
            fr.write(response.content)
        print(downLoadImageUrl, "该图片下载成功！")
        count+=1

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests
# import csv
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# import os
# import re
# import json
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import requests,lxml.etree
# import urllib.parse
# import urllib.request
# from string import digits
#
#
#
# if __name__ == '__main__':
#     # 打开浏览器
#     chromedriver = "D:\\chromedriver.exe" #这里写本地
#     os.environ["webdriver.Chrome.driver"] = chromedriver #调用chrome浏览器
#     url = 'https://gs.amac.org.cn/amac-infodisc/res/pof/person/personList.html?userId=1700000000699069'
#     # url = 'https://jiapu.library.sh.cn/#/jiapu:STJP000019'
#     driver = webdriver.Chrome(chromedriver)
#     driver.get(url)
#     # driver.refresh() #刷新页面
#     driver.maximize_window() #浏览器最大化
#     driver.implicitly_wait(5)
#     tbody = driver.find_elements_by_xpath("//*[@id='dvccFundList']/tbody/tr")
#     print(len(tbody))
#     for i,row  in enumerate(tbody):
#         href = row.find_element_by_class_name("ajaxify").get_attribute('href')
#         print(href)
#         row.get(i).findElement(By.cssSelector("td:nth-child(1)> a")).click()
#     # 提取页面元素
#


