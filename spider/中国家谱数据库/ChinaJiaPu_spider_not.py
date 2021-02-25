import time
import numpy as np
from PIL import ImageGrab
import requests
import cv2
from selenium import webdriver
import os, time
import pytesseract
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

if __name__ == '__main__':
    f = open(file="D://中国家谱数据库于氏.txt", mode='r', encoding='utf-8')
    data = f.read()
    lists = data.split('\n')
    print(type(lists))
    f.close()
    print(lists)
    
    # 打开浏览器
    chromedriver = "D:\\chromedriver.exe"  # 你的本地driver的路径
    os.environ["webdriver.Chrome.driver"] = chromedriver  # 调用chrome浏览器
    driver = webdriver.Chrome(chromedriver)
    for item in lists:
        # url = 'http://gd.ccnu.edu.cn/genealogyHtml/detail?entityid=33078bab3b776c936d75f61e3582e9fa'
        arr = item.split("|")
        url = arr[0]
        year = arr[1]
        driver.get(url)
        # 添加Cookie
        driver.add_cookie({'name': '__guid', 'value': '10050019.2063385382769837000.1600302782260.3896'})
        driver.add_cookie({'name': 'Hm_lvt_bcd337de765536d8f667e2116b8d917e', 'value': '1613636560'})
        driver.add_cookie({'name': 'SESSION', 'value': '295a06b3-c7b1-4331-9302-0bf0792220b7'})
        driver.add_cookie({'name': 'Hm_lpvt_bcd337de765536d8f667e2116b8d917e', 'value': '1613704924'})
        driver.add_cookie({'name': 'monitor_count', 'value': '12'})
        # 再次打开页面刷新Cookie
        driver.get(url)

        # 族谱唯一id
        id = re.findall("(?<=entityid=).*", url)[0]
        # 提取页面元素
        driver.implicitly_wait(5)  # 属于隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时；
        time.sleep(5)  # 表示必须等待5秒定位
        # 地区
        district = driver.find_element_by_xpath("/html/body/main/div[2]/ul/li[1]/span").text
        # 谱名
        title = driver.find_element_by_xpath("/html/body/main/div[2]/ul/li[2]/span").text
        title = title.replace("于-", "")

        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/main/div[2]/div[4]/iframe"))
        # 页数
        page_size = driver.find_element_by_id("numPages").text
        page_size = re.findall("\\d+", page_size)[0]

        driver.find_element_by_id("presentationMode").click()
        time.sleep(5)
        # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
        pic_path = "D:\\ScreenPicture\\" + "【" + str(id) + "】" + district + "《" + title + "》" + "（" + year + ")" + "\\"
        print('目录：{}'.format(pic_path))
        isExists = os.path.exists(pic_path)
        if not isExists:
            os.makedirs(pic_path)
        count = 1
        for i in range(1, int(page_size) + 1):
            print('下载第{}张图片'.format(count))
            time.sleep(0.2)
            driver.save_screenshot(pic_path + str(count) + '.png')
            driver.find_element_by_id("viewer").click()
            count = count + 1
