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
    url = 'http://read.nlc.cn/OutOpenBook/OpenObjectBook?aid=892&bid=21264.0'
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


    #新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
    pic_path = "D:\\ScreenPicture\\国家图书馆\\"+"【"+str(412000003167)+"】"+"于氏宗譜"+"\\"
    print('目录：{}'.format(pic_path))
    isExists=os.path.exists(pic_path)
    if not isExists:
        os.makedirs(pic_path)
    count = 1
    for i in range(1,int(188)+1):
        # 提取页面元素
        # driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='myframe']"))
        print("Start  : %s" % time.ctime())
        time.sleep( 5 )
        print("End : %s" % time.ctime())
        print('下载第{}张图片'.format(count))
        driver.save_screenshot(pic_path+str(count)+'.png')
        # 提取页面元素
        driver.find_element_by_id("btnGotoNextPage").click()
        count =count+1
        time.sleep(5)

