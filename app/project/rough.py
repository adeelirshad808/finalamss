# # # importing required modules
# # from os import error
# # import PyPDF2
# # import difflib
# import difflib

# from difflib import SequenceMatcher
# with open(r"C:\Users\AdeeL\Desktop\AMS\app\project\file3.txt", errors="ignore") as file1, open(r"C:\Users\AdeeL\Desktop\AMS\app\project\file2.txt", errors="ignore") as file2:
#     file1_data = file1.read()
#     file2_data = file2.read()
#     print(difflib.SequenceMatcher(None, file1_data, file2_data).ratio()*100)

# from django.core.mail import send_mail

# subject = 'Thanks for registration'
# message = 'you have been registered succesfully'
# send_mail(subject, message, 'adeelirshad808@gmail.com',
#           'adeelirshad512@gmail.com')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pandas as pd
from bs4 import BeautifulSoup
from sklearn import preprocessing
import numpy as np
import re
import sqlalchemy as sq
from sqlalchemy import create_engine
import connection_variable as cv
from datetime import date


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)

url = 'https://www.google.com/maps/search/animal+clincs+islamabad/@33.7365747,73.0496682,13z/data=!3m1!4b1'
driver.get(url)
driver.implicitly_wait(5)

soup = BeautifulSoup(driver.page_source, "lxml")
date1 = soup.find_all(
    "div", {'class': "MVVflb-haAclf V0h1Ob-haAclf-d6wfac MVVflb-haAclf-uxVfW-hSRGPd"})
for a in date1:
    b = a.get("aria-label")
    print(b)
    c = a.find_all("div", {'class': "ZY2y6b-RWgCYc"})
    for f in c:
        d = f.find_all("span", {'jstcache': "92"})
        for e in d:
            print(e.text)
