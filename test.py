"""
    
get question attribute 되는지 시도해보기

extract.html 만들기, question context는 이미 있다고 생각
javascript 통해서 답변 안할거 아예 삭제

post 한 이후에는 답변한 table에 올리고
if 답변 불가능
    넘어가고 answered table에서 해당 답변 지우기

"""
import time
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime, timedelta

def printdate(startdate_str, enddate_str):
    startdate = datetime.strptime(startdate_str, '%Y-%m-%d')
    enddate = datetime.strptime(enddate_str, '%Y-%m-%d')
    dates = []
    # DateCheck DB 업데이트
    current_date = startdate
    while current_date <= enddate:
        if not current_date in dates:
            print(current_date)
        current_date += timedelta(days=1)

printdate('2023-03-01', '2023-03-05')