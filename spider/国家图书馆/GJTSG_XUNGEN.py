
from bs4 import BeautifulSoup
import requests
import csv
import ssl
import os
import re
import urllib.request
import json
import time
import base64

if __name__ == '__main__':
    proxies = {
        'http': '182.111.128.179:25239',
        'https': '182.111.128.179:25239'
    }
    token=""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
                'Cookie':'LOGIN=75756d782d3135303231363131323433; SCREEN_NAME=47356245556979656938374c47657752724265736c644b776838423477373270'

    }
    url = "http://ouroots.nlc.cn/view.html?41510488-1-1-1-%E8%95%AD%E5%B1%B1%E6%B9%98%E5%8D%97%E9%9F%93%E6%B0%8F%E5%AE%B6%E8%AD%9C-SZJP00001"
    base_str1 = re.findall("\\d{8}",url)[0]
    base_str2 = url.split('-')[-1]
    url_detail= "http://dsnode.ouroots.nlc.cn/gtService/data/catalogVolume?catalogKey="+base_str1+"&bookid="+base_str2
    res = requests.get(url=url_detail, headers=headers, timeout=5, verify=False)
    jsonstr = res.text
    volume = json.loads(jsonstr)['volume']
    for ob in volume:
        page = ob['pages']
        volumeId = ob['volumeId']
        count = 1
        for i in range(page):
            downLoadUrl = "http://dsnode.ouroots.nlc.cn/data/catalogImage?catalogKey=41510488&volumeId="+str(volumeId)+"&page="+str(i+1)+"&userKey=&token=IUIOO8GHY59AUGKOMKZWD2NU3LM938BBK3R6AY3YORUXQ6VH"
            response = requests.get(url=downLoadUrl, headers=headers, timeout=5, verify=False)
            image64_res = response.text
            image64 = json.loads(image64_res)['imagePath']
            image64_str = re.findall("(?<=base64,).*",image64)[0]
            print(downLoadUrl,"准备下载！")
            imagedata = base64.b64decode(image64_str)
            localPath  = "D:\\GJTSG\\"+"卷"+str(volumeId)+"\\"
            isExists=os.path.exists(localPath)
            if not isExists:
                os.makedirs(localPath)
            file = open(localPath+str(count)+".jpg","wb")
            file.write(imagedata)
            file.close()
            count += 1
