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

if __name__ == '__main__':
    f = open("F://myImages//Cookie.txt", 'r', encoding='utf-8')
    cookie = f.read()
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":cookie
    }
    proxies = {
        "https":"http://175.43.35.57:9999"
    }
    f = open("F://myImages//8.txt", 'r', encoding='utf-8')
    data = f.read()
    f.close()
    images = json.loads(data)['images']
    print(len(images))
    count = 1
    for index,image in enumerate(images):
        # if(index<2002):
        #     continue
        url= image
        # sub_str= re.findall("61903/(.*?)(?=\\?)",url)[0]
        sub_str= re.findall("61903/(.*?)\\/image",url)[0]
        downLoadImageUrl = 'https://sg30p0.familysearch.org/service/records/storage/deepzoomcloud/dz/v1/'+sub_str+'/.jpg'
        print(downLoadImageUrl)
        localPath  = "F:\\myImages\\【2212605】浦陽汪山于氏宗譜[4卷]-中國, 浙江省, 浦江縣\\汪山于氏宗譜 四卷, 4\\"
        isExists=os.path.exists(localPath)
        if not isExists:
            os.makedirs(localPath)
        response = requests.get(url=downLoadImageUrl, headers=headers,verify=False,timeout=15)

        with open(localPath+str(count)+".jpg", 'wb') as f:
            f.write(response.content)
        count += 1
        print(downLoadImageUrl, "该图片下载成功！")
