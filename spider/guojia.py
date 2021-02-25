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

if __name__ == '__main__':
    # 打开浏览器
    chromedriver = "D:\\chromedriver.exe" #这里写本地
    os.environ["webdriver.Chrome.driver"] = chromedriver #调用chrome浏览器
    url = 'http://read.nlc.cn/OutOpenBook/OpenObjectBook?aid=892&bid=215733.0'
    # url = 'https://jiapu.library.sh.cn/#/jiapu:STJP000019'
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    # driver.refresh() #刷新页面
    driver.maximize_window() #浏览器最大化
    driver.implicitly_wait(5)
    driver.find_element_by_id("username").send_keys("15021611243")
    driver.find_element_by_id("password").send_keys("200811")
    driver.find_element_by_class_name("yzimg")
    print(driver.find_element_by_class_name("yzimg").get_attribute('src'))
    driver.find_element_by_class_name("loginbtn").click()
    # 提取页面元素
    # time.sleep(6)
    driver.implicitly_wait(5) #隐式等待5秒
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='myframe']"))
    for i in range(10):
        driver.implicitly_wait(5) #隐式等待5秒
        bbox = (400, 115, 1550, 1040)
        im = ImageGrab.grab(bbox)
        # 参数 保存截图文件的路径
        im.save(str(i)+'as.png')
        driver.find_element_by_css_selector("[class='fwr-toolbar-page-icons fwr-toolbar-page-next']").click()
        # driver.find_element_by_class_name("fa fa-3x fa-chevron-left").click()
        # driver.find_element_by_xpath("//*[@id='workspace-cb0a201d-33aa-4d22-80c6-1ccffa983d2e']/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/a[1]")


     # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    # bbox = (200, 200, 600, 600)

