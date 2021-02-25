import time
import numpy as np
from PIL import ImageGrab
import pyautogui
import cv2
from selenium import webdriver
import os,time
import pytesseract
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

if __name__ == '__main__':
    # 打开浏览器
    chromedriver = "D:\\chromedriver.exe" #这里写本地
    os.environ["webdriver.Chrome.driver"] = chromedriver #调用chrome浏览器
    url = 'https://www.zupu.cn/zp/39446/view'
    # url = 'https://jiapu.library.sh.cn/#/jiapu:STJP000019'
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    # driver.refresh() #刷新页面
    driver.maximize_window() #浏览器最大化
    driver.implicitly_wait(5)
    driver.find_element_by_id("userId").send_keys("yuyangcq@163.com")
    driver.find_element_by_id("password").send_keys("yuyang2008")
    driver.find_element_by_class_name("btn-login").click()
    # 提取页面元素
    driver.implicitly_wait(5) #隐式等待5秒
    time.sleep(5)
    # 地区
    district = driver.find_element_by_xpath("/html/body/main/div[2]/ul/li[1]/span").text
    #谱名
    title = driver.find_element_by_xpath("/html/body/main/div[2]/ul/li[2]/span").text
    driver.switch_to.frame(driver.find_element_by_xpath("/html/body/main/div[2]/div[4]/iframe"))
    # 页数
    page_size = driver.find_element_by_id("numPages").text
    page_size= re.findall("\\d+",page_size)[0]

    driver.find_element_by_id("presentationMode").click()
    driver.implicitly_wait(5) #隐式等待5秒
    time.sleep(5)
    #新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
    pic_path = "D:\\ScreenPicture\\"+"【"+str(id)+"】"+district + title+"\\"
    print('目录：{}'.format(pic_path))
    isExists=os.path.exists(pic_path)
    if not isExists:
        os.makedirs(pic_path)
    count = 1
    for i in range(1,int(page_size)+1):
        print('下载第{}张图片'.format(count))
        driver.save_screenshot(pic_path+str(count)+'.png')
        driver.find_element_by_id("viewer").click()
        count =count+1


