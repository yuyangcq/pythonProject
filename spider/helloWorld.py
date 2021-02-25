import random
import urllib.request
import json
import requests
ippools=[


]
def ip(ippools):
    ippools=[


    ]
    proxyUrl = "https://www.wanbianip.com/Users-getStaticIpListNew.html?appid=2609&appkey=a6a715b760c07fea9e789672a5065aa4&pageRowsNum=20&pageIndex=1&province=&city=&getSocksPort=0"
    response = requests.get(url=proxyUrl).text
    proxyIpList = json.loads(response)['data']
    for i, val in enumerate(proxyIpList):
        ippools.append(val['IP']+":"+str(val['Port']))
    print('当前代理池：{}'.format(ippools))
    thisip=random.choice(ippools)
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,5):
    try:
        ip(ippools)
        url="http://www.baidu.com"
        data1=urllib.request.urlopen(url).read()
        data=data1.decode("utf-8","ignore")
        print(len(data))
        fh=open("D:\\tang\\ip_baidu_"+str(i)+".html","wb")
        fh.write(data1)
        fh.close()
    except Exception as err:
        print(err)