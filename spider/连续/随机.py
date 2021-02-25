import random
import time
import numpy as np
from PIL import ImageGrab
import pyautogui
import cv2
from selenium import webdriver
import os,time
import pytesseract
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # 打开浏览器
    list1 = ['佛山', '南宁', '北海', '杭州', '南昌', '厦门', '温州']
    # 随机返回只有一个值的list
    choice_num=random.choice(list1)
    print(choice_num)
