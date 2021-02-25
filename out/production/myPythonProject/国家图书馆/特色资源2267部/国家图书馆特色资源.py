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
    pic_path = "F:\\爬虫\\国家图书馆\\"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    url = 'http://mylib.nlc.cn/system/application/search/display/metaDataDisplayRedirectPage.jsp?metaData.id=6528439&metaData.lId=3765800&IdLib=402834c3361e6e5001361ee3bb12004a'
    response = requests.get(url=url, headers=headers,verify=False,timeout=15)
    list_html = response.text
    soup = BeautifulSoup(list_html,'html.parser')
    divs = soup.find_all('div', class_='chapter_item')
    for div in divs:
        print("==========开始解析===========")
        volumes=div.find('div', class_='chapter_item_title highlightheader').get_text().replace("\t","").strip()
        print(volumes)
        onclick = div.find('input', class_='chapter_item_btn_read')['onclick']
        id= re.findall("\\('(.*?)',",onclick)[0]
        print('目录：{}'.format(pic_path))
        isExists=os.path.exists(pic_path)
        if not isExists:
            os.makedirs(pic_path)
        count = 1
        url = 'http://mylib.nlc.cn/system/doc/images/28005140/20170113_01/'+str(id)+'/1'
        print(url)
        print(pic_path+volumes+".zip")
        r = requests.get(url)
        with open(pic_path+volumes+".zip", "wb") as code:
            code.write(r.content)


