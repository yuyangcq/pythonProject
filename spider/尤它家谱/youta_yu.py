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
    ids=[]
    infos=[]
    url = "https://www.familysearch.org/records/images/api/rmsThin/search/group"
    data = {"pageNumber": "7", "pageSize": 50, "surname": "于"}
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"__guid=204302742.2942089552436081000.1599206340793.9126; fs-revisit=1; s_ecid=MCMID%7C24202284965941722571286861290281951950; _cs_c=1; WRUIDAWS=2934964561904987; _CT_RS_=Recording; _cs_id=0126abed-e700-a3f4-be0f-74adef869b64.1599206419.1.1599206776.1599206419.1586096378.1633370419975.Lax.0; __CT_Data=gpv=1&ckp=tld&dm=familysearch.org&apv_42_www04=4&cpv_42_www04=4&rpv_42_www04=4; ctm={'pgv':8370013373422899|'vst':2880983047587349|'vstr':8016870583344568|'intr':1599206777104|'v':1}; fslanguage=zh; fs-tf=1; notice_behavior=implied|us; AMCVS_66C5485451E56AAE0A490D45%40AdobeOrg=1; s_cc=true; JSESSIONID=247B2E1C2395BE225B1F3B31DE974865; fs_search_history=https%3A//www.familysearch.org/search/catalog/results%3Fcount%3D20%26placeId%3D918788%26query%3D%252Btitle%253A%25E4%25BC%259A%25E8%25AF%2595; mbox=PC#46853acceb5b4d08b6bf252965a31cbf.38_0#1662719160|session#2244f903188a4bca8b65e4f009abccc7#1599476220; s_sq=%5B%5BB%5D%5D; fssessionid=5e7c4507-1d0d-4d46-92fd-4ce61aac3adb-prod; fsrefreshtoken=-3515823-74-16-12597-36-948452-14364600125-25-111111-1088084-49-74-110-6178113-43-113; fs_experiments=u%3Dqqyzy%2Ca%3Dshared-ui%2Cs%3Dd0ba994d70ad7d30020a84e9ab7f4e5a%2Cv%3D1111101111000000000000000001011010000100111001000110011011111000001001010111111110110011011100000%2Cb%3D91%26a%3Dhome%2Cs%3D498ccc0cb32c7bd4fd350ddd136397ab%2Cv%3D0010100000110000000001101001011001111110010010000000001000011010010000%2Cb%3D98%26a%3Dtree-v8%2Cs%3D5469aeea947fb85690f8a00909929302%2Cv%3D1011100101101100000110%2Cb%3D69%26a%3Dstyleguide%2Cs%3D%2Cv%3D%2Cb%3D48%26a%3Dregistration%2Cs%3D92f2470df5e82d129e02045034fea22a%2Cv%3D101110001011101010111001111110110101101000100011%2Cb%3D74%26a%3Dlightyear-image-search%2Cs%3Dadeaf98e982a7682f912115420801672%2Cv%3D00110000000011001000101000101010100111110010101101100%2Cb%3D92%26a%3Dhf-inj%2Cs%3Da5c58239b27e7a1695452b08401b5bfd%2Cv%3D0%2Cb%3D12%26a%3Dsearch-artifact%2Cs%3Dc2b3186c655f7b456295d36bcf5def03%2Cv%3D1100101111010000001011011010001010001%2Cb%3D40%26a%3Dsearch-react%2Cs%3D3b4b90fcaff1adbe5fd7876fed384b3a%2Cv%3D1100%2Cb%3D22%26a%3Dsearch-bifrost%2Cs%3Ddedb6f5e7435b5aba342c92effe35c81%2Cv%3D1101000101001010011%2Cb%3D29%26a%3Dask%2Cs%3D5eb79a8483cf31541935692df363a923%2Cv%3D011011011111010110001101001101011000000010000000000000000000011%2Cb%3D9%26a%3Dhelp%2Cs%3Dbc1a858154b4928b7b565dabb836f997%2Cv%3D01101100011%2Cb%3D7; monitor_count=9; utag_main=v_id:0174582040d1000152af868b14d71006e002006600bd0$_sn:29$_ss:1$_st:1600218802913$ctsplit2:51$vapi_domain:familysearch.org$ses_id:1600217002913%3Bexp-session$_pn:1%3Bexp-session; AMCV_66C5485451E56AAE0A490D45%40AdobeOrg=1585540135%7CMCMID%7C24202284965941722571286861290281951950%7CMCAAMLH-1600821803%7C11%7CMCAAMB-1600821803%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1600224203s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; s_ppvl=FamilySearch%253A%2520Lightyear-Image-Search%253A%2520Image%2520Search%2520Results%2C100%2C100%2C4926%2C1872%2C395%2C1920%2C1080%2C1%2CL; s_ppv=FamilySearch%253A%2520Lightyear-Image-Search%253A%2520Image%2520Search%2520Results%2C100%2C100%2C830%2C1872%2C427%2C1920%2C1080%2C1%2CL"
    }
    proxies = {
        "http":"http://115.218.0.214"
    }
    res = requests.post(url=url, data=data, headers=headers)
    jsonstr = res.text
    if len(json.loads(jsonstr)['rows']) > 0:
        rows = json.loads(jsonstr)['rows']
        for index,row in enumerate(rows):
            if(index<=21):
                continue
            info= row['coverageItems'][0]['place']['info']
            ids.append(row['id'])
            infos.append(info)
            local_dir  = "F:\\myImages\\7\\"+"【"+str(row['id'])+"】"+info+"\\"
            print(local_dir)
            isExists=os.path.exists(local_dir)
            if not isExists:
                os.makedirs(local_dir)
            detailUrl = 'https://www.familysearch.org/records/images/api/rmsThin/group/'+row['id']+'/children'
            print(detailUrl)
            count = 1
            res = requests.get(url=detailUrl, headers=headers,proxies=proxies)
            jsonstrDetail = res.text
            deepZoomBaseUrl=json.loads(jsonstrDetail)['deepZoomBaseUrl']
            if len(json.loads(jsonstrDetail)['images']) > 0:
                images = json.loads(jsonstrDetail)['images']
                for imageStr in images:
                    downLoadImageUrl = deepZoomBaseUrl+str(imageStr)+'/.jpg'
                    print(downLoadImageUrl)
                    localPath = local_dir +str(count)+ '.jpg'
                    try:
                        pic = requests.get(downLoadImageUrl, headers=headers,proxies=proxies)
                    except requests.exceptions.ConnectionError:
                        print('图片无法下载')
                    fp = open(localPath, 'wb')
                    fp.write(pic.content)
                    fp.close()
                    print(downLoadImageUrl, "该图片下载成功！")
                    count += 1


