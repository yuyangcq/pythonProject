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
import shutil, os
import re
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests, lxml.etree
import urllib.parse
import urllib.request
import pathlib

def copy_file(source, target):
    for filename in os.listdir(source):
        filename_s = source + os.sep + filename
        filename_t = target + os.sep + filename
        if os.path.isdir(filename_s):
            if not os.path.exists(filename_t):
                os.mkdir(filename_t)  # 在目标文件夹中创建对应的文件夹
            copy_file(filename_s, filename_t)  # 递归
        else:
            print('[*]  Source :', filename_s)
            print('[*]  Target :', filename_t)
            with open(filename_s, 'rb') as f_s:
                with open(filename_t, 'wb') as f_t:
                    f_t.write(f_s.read())

if __name__ == '__main__':  # 主函数，输入源文件路径和目标文件路径
    source = r'S:\source'
    target = r'S:\target'
    copy_file(source, target)
