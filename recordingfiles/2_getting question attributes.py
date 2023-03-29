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

def goToWaitingPage():
    
    global browser, service, options

    # find driver
    service = Service('.\chromedriver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(service=service, options=options)

    # navigate to the website
    browser.get('https://tzone.megastudy.net/')

    # find and click the first element
    first_element = browser.find_element(By.XPATH, '/html/body/form/div/div[1]/label[2]/input')
    first_element.click()

    # find and input text into the second element
    second_element = browser.find_element(By.ID, 'id')
    second_element.send_keys('heeseopark')

    browser.implicitly_wait(10)

    # find and click the third element
    third_element = browser.find_element(By.ID, 'sp_smsct')
    third_element.click()

    browser.implicitly_wait(10)

    # find and input text into the fourth element
    fourth_element = browser.find_element(By.ID, 'passwd')
    fourth_element.send_keys('heeseo1099')

    browser.implicitly_wait(10)

    # find and click the fifth element
    fifth_element = browser.find_element(By.ID, 'sp_login')
    fifth_element.click()

    browser.implicitly_wait(10)

    # find and click the sixth element
    sixth_element = browser.find_element(By.ID, 'a594')
    sixth_element.click()

    browser.implicitly_wait(10)

    # find and click the seventh element
    seventh_element = browser.find_element(By.ID, 'aa4233')
    seventh_element.click()

    #go into iframe
    wait = WebDriverWait(browser, 2)
    iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

    # Switch to the iframe element
    browser.switch_to.frame(iframe)
    browser.implicitly_wait(10)


    # find and click the eighth element
    eighth_element = browser.find_element(By.XPATH, '/html/body/div[1]/a')
    eighth_element.click()

    # Move to the next tab
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.TAB)
    browser.switch_to.window(browser.window_handles[-1])

    time.sleep(2)





def paging(function):

    while True:
        # Check if the element with id 'nextpage' exists
        try:
            wait = WebDriverWait(browser, 1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/a[11]')))

            function()

            for i in range(2,11):
                browser.find_element(By.XPATH, f'/html/body/div[3]/div[3]/div/a[{i}]').click()
                browser.implicitly_wait(10)

                function()

            browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/a[11]').click()
            browser.implicitly_wait(10)

        except TimeoutException:
        # If the element doesn't exist, just increment through the pages
            function()

            page_number = 1
            while True:
                try:
                    wait = WebDriverWait(browser, 1)
                    wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div/a[{page_number+1}]'))).click()
                    # Do something with current_element

                    function()

                    page_number += 1
                except TimeoutException:
                    break
            break


def goingThroughTotalPage():


    current_element_number = 1

    while True:
        # Click element if the current element is clickable
        try:
            wait = WebDriverWait(browser, 1)
            wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[2]/table/tbody/tr[{current_element_number}]/td[5]/a'))).click()

        except TimeoutException:

            break
            
        # Do something with the current element
        printattributes()
        
        # Go Back to Total Page
        time.sleep(0.5)
        browser.back()

        # Move to the next element
        current_element_number += 1


import re

def getPageNum(text):
    pattern1 = r'\b(\d+)\s*[pP][gG]?[.]?\s*'
    pattern2 = r'\b(\d+)[pP][gG]?[.]?\s*'
    pattern3 = r'\b(\d+)[pP]?[.]?\s*'
    pattern4 = r'\b(\d+)\s*(?:페|페이지|쪽)[.]?\s*$'
    pattern5 = r'(?:^|\D)(\d+)\s*(?:페이지)\s*'

    for pattern in [pattern1, pattern2, pattern3, pattern4, pattern5]:
        match = re.search(pattern, text)
        if match:
            num_str = match.group(1)
            if num_str.strip() == '' or num_str.strip() != num_str:
                return None
            return int(num_str)
    return None


def getQuestionNum(text):
    pattern1 = r'(?<!\S)(\d{1,3})\s*[번 ]'
    pattern2 = r'(?:^|\W)(?:예|예제)?\s*(\d{1,3})\s*(?:번)?'


    for pattern in [pattern1, pattern2]:
        match = re.search(pattern, text)
        if match:
            num_str = match.group(1)
            if num_str.strip() == '' or num_str.strip() != num_str:
                return None
            return int(num_str)
    
    return None




def getThemeNum(text):
    pattern = r'(?:^|[^0-9])(\d{1,2})\s*(?:띰|theme)'
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        return None


def printattributes():
    # Get book title
    book_title = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[1]/strong').text

    # Get question_id
    question_id = int(browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[2]').text)
    
    # Get page, question, and theme numbers
    page_num = getPageNum(book_title)
    question_num = getQuestionNum(book_title)
    theme_num = getThemeNum(book_title)
    print(f'{book_title}')

    print(f'id:{question_id}, page:{page_num}, question:{question_num}, theme:{theme_num}')

def updateSearchedAndFaqTable():

    goToWaitingPage()

    print('finish goToWaitingPage')

    
   

    paging(goingThroughTotalPage)


updateSearchedAndFaqTable()