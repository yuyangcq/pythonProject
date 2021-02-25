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


def check(userName,count):
    user_name_temp = userName
    if os.path.exists(localPath+userName+".jpg")==False:  # 判断图片名称是否存在
        print("{}不存在".format(user_name_temp))
        return user_name_temp
    else:
        print("{}存在".format(user_name_temp))
        remove_digits = str.maketrans('', '', digits)
        userName = userName.translate(remove_digits)
        user_name_temp=userName+str(count)
        count+=1
        return check(user_name_temp,count)


if __name__ == '__main__':
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"__guid=128030490.2831871680830658600.1597218666700.9712; monitor_count=27"
    }
    proxies = {
        "https":"https://171.35.171.227:9999",
        "http":"http://171.35.171.227:9999"
    }
    f = open("F://my.txt", "r")
    data = f.read()
    arr= data.split(',\n')
    print(arr)
    f.close()
    page=0

    for url in arr:
        count = 1
        id = re.findall("(?<=accountId=).*",url)[0]
        detail_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/person/"+id+"?rand=0.9426538075937674"
        res = requests.get(url=detail_url, headers=headers,verify=False,timeout=5)
        jsonstr = res.text
        userName = json.loads(jsonstr)['userName']
        downLoadImageUrl = json.loads(jsonstr)['personPhotoBase64']
        print(downLoadImageUrl)
        localPath  = "F:\\图片\\"
        isExists=os.path.exists(localPath)
        if not isExists:
            os.makedirs(localPath)
        # user_name_result = check(userName,count)
        response = requests.get(url=downLoadImageUrl, headers=headers,verify=False,timeout=5)
        with open(localPath+userName+".jpg", 'wb') as fr:
            fr.write(response.content)
        print(downLoadImageUrl, "该图片下载成功！")


