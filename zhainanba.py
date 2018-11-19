# -*- coding:UTF-8 -*-

import urllib
import time
import os
import sys
import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import win32api
import win32con

VK_CODE = {'enter': 0x0D, 'down_arrow': 0x28}


# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)


# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


def schedule(a, b, c):
    # a:已下载的数据块 b:数据块的大小 c:远程文件的大小
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


url = "https://bbs.zhain.net/thread-574-1-1.html"

headers = {
    "Referer": "https://bbs.zhain.net/thread-574-1-1.html",
    "User-": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.2.3.4000"
}
response = requests.get(url, headers=headers).text

files = re.findall(r'file="(.*?)"', response)
# with open("znb.txt", "w") as f:
#     f.write(response)
print(files)

browser = webdriver.Chrome()
for index, f in enumerate(files):
    browser.get(f)
    elem = browser.find_element_by_xpath("//img")
    action = ActionChains(browser).move_to_element(elem)
    action.context_click(elem)  # 右键
    action.perform()

    time.sleep(1)
    # 按v
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)
    # 按enter
    keyDown("enter")
    keyUp("enter")
    time.sleep(1)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import win32api
import win32con

VK_CODE = {'enter': 0x0D, 'down_arrow': 0x28}


# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)


# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


print('Please wait...Firefox loading...')
print('---------------------------------')
# 用浏览器实现访问
driver = webdriver.Firefox()
driver.get("一个url")
element = driver.find_element_by_id('img').find_element_by_tag_name('img')
img_url = element.get_attribute('src')
# print(img_url)
action = ActionChains(driver).move_to_element(element)
action.context_click(element).perform()
time.sleep(1)
# 按v
win32api.keybd_event(86, 0, 0, 0)
win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
# 按enter
keyDown("enter")
keyUp("enter")
time.sleep(1)





