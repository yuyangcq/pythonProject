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

    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        "Cookie":"s_ecid=MCMID%7C37877496981810042992032584305905995170; fs-revisit=1; s_fid=7ABF3E96A402E3DE-2E8CEEC0B916D979; fs-tf=1; notice_behavior=implied|us; AMCVS_66C5485451E56AAE0A490D45%40AdobeOrg=1; AMCV_66C5485451E56AAE0A490D45%40AdobeOrg=1585540135%7CMCMID%7C37877496981810042992032584305905995170%7CMCAAMLH-1601374775%7C11%7CMCAAMB-1601374775%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1600777175s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0%7CMCSYNCSOP%7C411-18531; s_cc=true; s_ppvl=https%253A%2F%2Fwww.familysearch.org%2Fsearch%2Fcatalog%2F1084768%253Favailability%253DFamily%252520History%252520Library%2C91%2C91%2C1298.2222290039062%2C2133%2C1076%2C1920%2C1080%2C0.9%2CL; s_ppv=FamilySearch%253A%2520Account%253A%2520Sign%2520In%2520to%2520FamilySearch%2C90%2C90%2C969%2C1920%2C969%2C1920%2C1080%2C1%2CL; ADRUM=s=1600769998630&r=https%3A%2F%2Fident.familysearch.org%2Fcis-web%2Foauth2%2Fv3%2Fauthorization%3F1344571278; s_sq=see-extensions%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.familysearch.org%25252Fsearch%25252Fcatalog%25252Fresults%25253Fcount%25253D20%252526query%25253D%2525252Bkeywords%2525253A%252525E4%252525B9%252525A1%252525E8%252525AF%25252595%2526link%253D1200%252520%2525281%252529%2526region%253Dyear0-1200%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fwww.familysearch.org%25252Fsearch%25252Fcatalog%25252Fresults%25253Fcount%25253D20%252526query%25253D%2525252Bkeywords%2525253A%252525E4%252525B9%252525A1%252525E8%252525AF%25252595%2526oid%253Dhttps%25253A%25252F%25252Fwww.familysearch.org%25252Fsearch%25252Fcatalog%25252Fresults%25253Fcount%25253D20%252526query%25253D%2525252Bkeywords%2525253A%252525E4%252525B9%252525A1%252525E8%252525AF%25252595%252526%2526ot%253DA%26ldsfchglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DFamilySearch%25253A%252520Account%25253A%252520Sign%252520In%252520to%252520FamilySearch%2526link%253D%2525E7%252599%2525BB%2525E5%2525BD%252595%2526region%253DeventForm%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DFamilySearch%25253A%252520Account%25253A%252520Sign%252520In%252520to%252520FamilySearch%2526pidt%253D1%2526oid%253D%2525E7%252599%2525BB%2525E5%2525BD%252595%2526oidt%253D3%2526ot%253DSUBMIT; fs_search_history=https%3A//www.familysearch.org/search/catalog/results%3Fcount%3D20%26query%3D%252Bkeywords%253A%25E4%25B9%25A1%25E8%25AF%2595%26offset%3D20; fssessionid=7e4137c0-be1b-4e9f-9a40-e7afa58b2f98-prod; fsrefreshtoken=-1524-6835-13-1068210629-55-1151-93-126-11385-55-42-77105116-100-109-12611331755732-18-83; fs_experiments=u%3Dqqyzy%2Ca%3Dshared-ui%2Cs%3D200b481b4e02b0d9cd60bda0ed31b1a6%2Cv%3D1111101111000000000000000001111010000100111001000110011011111000001001010111111110110011011100000%2Cb%3D19%26a%3Dlightyear-image-search%2Cs%3Dadeaf98e982a7682f912115420801672%2Cv%3D00110000000011001000101000101010100111100010101101100%2Cb%3D82%26a%3Dsearch-bifrost%2Cs%3Df5c22d1aa212e2a66431d6f398d2d0ae%2Cv%3D1101000101001010011000%2Cb%3D20%26a%3Dtree-v8%2Cs%3D943cb9200605fd9e0032c798afea63bd%2Cv%3D10111001011011000001100%2Cb%3D6; mbox=PC#ee409d09658e4ac99b2d890dd5a7ec42.38_0#1664151915|session#099fee64f44248cba35528efea10fb70#1600908975; utag_main=v_id:017466e12e350028458b212730740307202c606a00bd0$_sn:42$_ss:0$_st:1600908915124$ctsplit2:48$vapi_domain:familysearch.org$ses_id:1600907106106%3Bexp-session$_pn:3%3Bexp-session; ADRUM_BTa=R:77|g:e3859c51-3623-4ecc-8a58-02d27e2b98a7|n:familysearch_5aad8bfe-9311-4114-af23-41b5bf73eba5; ADRUM_BT1=R:77|i:243413|e:14|d:15"
    }
    proxies = {
        "https":"http://175.43.35.57:9999"
    }
    f = open("F://myImages//3.txt", 'r', encoding='utf-8')
    data = f.read()
    f.close()
    images = json.loads(data)['images']
    print(len(images))
    count = 1
    for index,image in enumerate(images):
        # if(index<959-1):
        #     continue
        url= image
        sub_str= re.findall("61903/(.*?)\\/image",url)[0]
        downLoadImageUrl = 'https://sg30p0.familysearch.org/service/records/storage/deepzoomcloud/dz/v1/'+sub_str+'/.jpg'
        print(downLoadImageUrl)
        localPath  = "F:\\myImages\\山東鄉試題名錄  (光緒28[1902]補行庚子[1900]辛丑[1901]丑恩正併科)\\"
        isExists=os.path.exists(localPath)
        if not isExists:
            os.makedirs(localPath)
        response = requests.get(url=downLoadImageUrl, headers=headers,verify=False,timeout=15)

        with open(localPath+str(count)+".jpg", 'wb') as f:
            f.write(response.content)
        count += 1
        print(downLoadImageUrl, "该图片下载成功！")
