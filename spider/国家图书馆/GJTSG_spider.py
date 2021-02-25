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
import time
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pyquery import PyQuery as pq



def proxyCircle():
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"name=value; LFR_SESSION_STATE_28005140=1601445780456; name=value; LFR_SESSION_STATE_28005140=1601444542910; name=value; LFR_SESSION_STATE_28005140=1601441773388; Hm_lvt_2cb70313e397e478740d394884fb0b8a=1599196477,1599456069,1599640078,1600734405; COOKIE_SUPPORT=true; __guid=54981559.3691288393625096700.1601438058926.3628; name=value; ticket='ticketId:TGC-421894-L8PbBf9ePZutBOMXV08jgX0GVFNSoYJgkoKKycTflwpbthasRs*version:v1.0*userAccount:15021611243*sessionid:C38764D11CC077276C3EDCE358D0088D*loginPlace:A100000NLC*createTime:1601438129439*validTime:1601445329439*'; JSESSIONID=0000aBq4pOZH5PZTmlOsFTMP9YT:-1; COMPANY_ID=1; NEW_ID=51474c394547364b5574585373496641654d4f3971513d3d; PASSWORD=3370665637724336506b673d; LOGIN=75756d782d3135303231363131323433; SCREEN_NAME=47356245556979656938374c47657752724265736c644b776838423477373270; GUEST_LANGUAGE_ID=simplified_CHINESE; bdshare_firstime=1601438136730; monitor_count=132"
    }

    url="http://mylib.nlc.cn/system/application/search/display/metaDataDisplayRedirectPage.jsp?metaData.id=6528444&metaData.lId=3765805&IdLib=402834c3361e6e5001361ee3bb12004a"
    res = requests.get(url, headers=headers,verify=False)
    html = res.text

    # d2 = pq(html)
    soup = BeautifulSoup(html, 'html.parser')   #文档对象
    # 类名为xxx而且文本内容为hahaha的div
    for k in soup.find_all('input',class_='chapter_item_btn_read'):
        print(k['onclick'])
        first = re.findall("goPlayer\\('(.*?)',",k['onclick'])[0]
        second = re.findall(",'(.*?)'\\)",k['onclick'])[0]
        print(first)
        print(second)
        pdf_url = "http://mylib.nlc.cn/web/guest/search/zhengjijiapu/medaDataObjectDisplay?metaData.id="+str(second)+"&metaData.lId="+str(first)+"&IdLib=402834c3361e6e5001361ee3bb12004a"

    # for k in soup.select("div[class=metadata_button_container] > div[class=chapter_item_title highlightheader]"):
    #     print(k)

    # print(soup)


if __name__ == '__main__':
    proxyCircle()

# for k in soup.find_all('a'):
#     print(k)
#     print(k['class'])#查a标签的class属性
#     print(k['id'])#查a标签的id值
#     print(k['href'])#查a标签的href值
#     print(k.string)#查a标签的string
#     #tag.get('calss')，也可以达到这个效果