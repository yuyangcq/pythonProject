
from bs4 import BeautifulSoup
import requests
import csv
import ssl
import os
import re
import urllib.request
import json
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
    proxies = {
        "http":"http://27.150.127.195:28803"
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    f = open("D://stjp//STJPID_3001-4000.txt", "r")
    data = f.read()
    arr= data.split(',\n')
    print(type(arr))
    f.close()
    print(arr)
    for id in arr:
        url = "https://fullimg.library.sh.cn/manifests/jiapu/"+id+".json"
        res = requests.get(url, headers=headers,verify=False)
        jsonstr = res.text
        structures = json.loads(jsonstr)['structures']
        my_file = json.loads(jsonstr)['label']
        print(my_file+'一共有：{}册'.format(len(structures)))
        for structure in structures:
            count = 1
            label = structure['label']
            localPath  = "D:\\stjp\\"+"【"+str(id)+"】"+my_file+"\\"+label+"\\"
            print('目录：{}'.format(localPath))
            isExists=os.path.exists(localPath)
            if not isExists:
                os.makedirs(localPath)
            canvases = structure['canvases']
            for canvase in canvases:
                base_str= re.findall("canvas/(.*?)\\.json",canvase)[0]
                downLoadImageUrl = "http://fullimg.library.sh.cn/iiif/jiapu/"+id+"/"+base_str+".tif/full/full/0/default.jpg"
                print(downLoadImageUrl,"准备下载！")
                response = requests.get(url=downLoadImageUrl, headers=headers,verify=False,timeout=15)
                with open(localPath+str(count)+".jpg", 'wb') as f:
                    f.write(response.content)
                count += 1
