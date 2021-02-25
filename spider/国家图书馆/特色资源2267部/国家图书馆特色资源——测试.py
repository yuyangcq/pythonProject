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
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    flag = 0
    # 打开浏览器
    chromedriver = "D:\\chromedriver.exe" #你的本地driver的路径
    os.environ["webdriver.Chrome.driver"] = chromedriver #调用chrome浏览器

    f = open("F://爬虫\国家图书馆//国家图书馆url.txt", "r", encoding='UTF-8')
    data = f.read()
    arrs= data.split('\n')
    f.close()
    for arr in arrs:
        str= arr.split('|')
        name = str[0]
        url = str[1]
        title_id= re.findall("(?<=metaData.id=)(.*?)(?=&metaData)",url)[0]
        # volume=re.findall("(?<=metaData.lId=)(.*?)(?=&IdLib)",url)[0]
        print(name)
        print(url)

        if flag== 0 :
            driver = webdriver.Chrome(chromedriver)
            driver.get(url)
            driver.implicitly_wait(5)
            driver.find_element_by_class_name("link-regist").click()
            driver.implicitly_wait(5)
            driver.find_element_by_id("username").send_keys("15021611243")
            driver.find_element_by_id("password").send_keys("200811")
            driver.find_element_by_id("login-button").click()
        time.sleep(1)
        flag = 1;
        driver.get(url)
        # 添加Cookie
        # driver.maximize_window() #浏览器最大化

        time.sleep(1)
        # 获取打开的多个窗口句柄
        windows = driver.window_handles

        pic_path = "F:\\爬虫\\国家图书馆\\"+"【"+title_id+"】"+name+"\\"
        cookie ='LOGIN=75756d782d3135303231363131323433; SCREEN_NAME=47356245556979656938374c47657752724265736c644b776838423477373270; Hm_lvt_2cb70313e397e478740d394884fb0b8a=1607412448,1607929702; COMPANY_ID=1; NEW_ID=51474c394547364b5574585373496641654d4f3971513d3d; PASSWORD=3370665637724336506b673d; Hm_lpvt_2cb70313e397e478740d394884fb0b8a=1608001268; COOKIE_SUPPORT=true; __guid=54981559.253397441791361200.1608001278649.0764; name=value; ticket="ticketId:TGC-369732-dzTHw7peZZ0FjITETuhL03p5oIevha08Slb2qkS2um3KNLTES3*version:v1.0*userAccount:15021611243*sessionid:A4634C2081723C9C04EBDE6AE07DF0EB*loginPlace:A100000NLC*createTime:1608010254252*validTime:1608017454252*"; JSESSIONID=0000j7ZVj25OEKk_pkc-C--0SfE:-1; GUEST_LANGUAGE_ID=simplified_CHINESE; bdshare_firstime=160'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
                   'Cookie': cookie
                   }
        response = requests.get(url=url, headers=headers,verify=False,timeout=15)
        list_html = response.text
        soup = BeautifulSoup(list_html,'html.parser')
        divs = soup.find_all('div', class_='chapter_item')

        if len(divs) != 0 :
            divs_open = driver.find_elements_by_css_selector("div[class=\"chapter_item\"]")
            for k in divs_open:
                k.find_element_by_css_selector("input").click()
                # 切换到当前最新打开的窗口
                time.sleep(2)
                driver.switch_to.window(windows[0])
        else:
            time.sleep(1)
            inputs_open = driver.find_element_by_css_selector("div[class=\"metadata_button_container\"]")
            inputs_open.find_element_by_css_selector("input[value=\"在线阅读\"]").click()

        if len(divs) != 0 :
            for div in divs:
                volumes=div.find('div', class_='chapter_item_title highlightheader').get_text().replace("\t","").strip()
                print(volumes)
                onclick = div.find('input', class_='chapter_item_btn_read')['onclick']
                id= re.findall("\\('(.*?)',",onclick)[0]
                print('目录：{}'.format(pic_path))
                isExists=os.path.exists(pic_path)
                if not isExists:
                    os.makedirs(pic_path)
                count = 1
                url = 'http://mylib.nlc.cn/system/doc/images/28005140/20170113_01/'+id+'/1'
                print(url)
                print(pic_path+volumes+".zip")
                r = requests.get(url, headers=headers,verify=False)
                with open(pic_path+volumes+".zip", "wb") as code:
                    code.write(r.content)
        else:
            div = soup.find('div', class_='metadata_button_container')
            onclick = div.find('input', class_='btn_blue')['onclick']
            id= re.findall("\\('(.*?)',",onclick)[0]
            print('目录：{}'.format(pic_path))
            isExists=os.path.exists(pic_path)
            if not isExists:
                os.makedirs(pic_path)
            count = 1
            url = 'http://mylib.nlc.cn/system/doc/images/28005140/20170113_01/'+id+'/1'
            print(url)
            print(pic_path+"第一册"+".zip")
            r = requests.get(url, headers=headers,verify=False)
            with open(pic_path+"第一册"+".zip", "wb") as code:
                code.write(r.content)
        print("下载结束")
