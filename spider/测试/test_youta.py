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
from bs4 import BeautifulSoup

if __name__ == '__main__':
    f = open("F://myImages//Cookie.txt", 'r', encoding='utf-8')
    cookie = f.read()
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":cookie,
        "Content-Type": "application/json; charset=utf-8",
    }
    proxies = {
        "https":"http://175.43.35.57:9999"
    }



    getUrl='https://www.familysearch.org/search/catalog/1065207'

    list_response = requests.get(url=getUrl,headers=headers,verify=False,timeout=15)
    list_html= list_response.text
    soup = BeautifulSoup(list_html)
    script = soup.select('script[type="text/javascript"]')
    for sc in script:
        var = sc.string
        if "var data" in var:
            print("包含var data的script标签:",var)
            array= var.split(';\n')
            for arr in array:
                if "var data" in arr:
                    print("包含var data的数组有:",arr)
                    result = re.findall("(?<=var data = ).*",arr)[0]
                    print("正则匹配data:",result)
                    jsonData = json.loads(result)
                    film_note = jsonData['film_note']
                    title = jsonData['title'][0] # 族谱名称
                    titleno = jsonData['titleno'][0] # 族谱名称 唯一id
                    for film in film_note:
                        digital_film_no = film['digital_film_no'][0]
                        if len(digital_film_no)<9:
                            digital_film_no=digital_film_no.zfill(9)
                        detail_url = "https://www.familysearch.org/search/film/"+digital_film_no+"?cat="+titleno
                        print("需要爬取的详情url:",detail_url)
                        # payloadData数据
                        payloadData = {
                            "type": "film-data",
                            "args": {
                                "dgsNum": digital_film_no,
                                "locale": "zh",
                                "loggedIn": True,
                                "sessionId": "db61993a-678b-4a45-8de1-f9fc0c2eacce-prod",
                                "state":{
                                    "cat": titleno,
                                    "catalogContext": titleno,
                                    "imageOrFilmUrl": "/search/film/"+digital_film_no,
                                    "i": "224",
                                    "selectedImageIndex":224,
                                    "viewMode":"g"
                                },
                            }
                        }
                        postUrl='https://www.familysearch.org/search/filmdatainfo'
                        response = requests.post(url=postUrl, json=payloadData, headers=headers,verify=False,timeout=15)
                        content = response.text
                        jsonData1 = json.loads(content)
                        print(jsonData)




    # postUrl='https://www.familysearch.org/search/filmdatainfo'
    # response = requests.post(url=postUrl, json=payloadData, headers=headers,verify=False,timeout=15)
    # content = response.text
    # # json.dumps() 将python字典 转化为 字符串              dict转成str
    # s = json.dumps(content)
    # # json.loads() 将json格式数据 转换为 python字典类型    str转成dict
    # jsonData = json.loads(s)
    # jsonData1 = json.loads(content)
    # print(jsonData)
    # print(jsonData1)