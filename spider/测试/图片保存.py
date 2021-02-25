"""
2020.09.26:alian
改变图片的位深度
"""
import requests
import urllib

if __name__ == '__main__':
    src="https://www.yiban.cn/captcha/index"
    localPath  = "D:\\验证码\\"
    response = requests.get(url=src, verify=False,timeout=15)
    with open(localPath+str(1)+".jpg", 'wb') as f:
        f.write(response.content)
