from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import ssl
import os
import re
import urllib.request
import json

if __name__ == '__main__':
    # 确定要爬取数据的网址
    url = "https://www.zupu.cn/zhpk/listPhotos"
    count = 1
    for i in range(978):
        data = {"start": i, "limit": "1", "filmId": "12707"}
        res = requests.post(url=url, data=data)
        jsonstr = res.text
        if len(json.loads(jsonstr)['data']) > 0:
            downLoadImageUrl = json.loads(jsonstr)['data'][0]['imgUrl']
            localPath = "F:\myImages\zupu"
            urllib.request.urlretrieve(downLoadImageUrl, f"{localPath}\\{count}.jpg")
            print(downLoadImageUrl, "该图片下载成功！")
            count += 1
            # print("图片已经全部下载完成，请前往", localPath, "查看！")
