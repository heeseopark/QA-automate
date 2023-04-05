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

def goToTotalPage():
    global browser, service, options
    # find driver
    service = Service('.\chromedriver\chromedriver.exe')
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(service=service, options=options)

    # navigate to the website
    browser.get('https://tzone.megastudy.net/')

    # find and click the first element
    first_element = browser.find_element(By.XPATH, '/html/body/form/div/div[1]/label[2]/input')
    first_element.click()

    browser.implicitly_wait(10)

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
    seventh_element = browser.find_element(By.ID, 'aa4231')
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
        printbook()
        
        # Go Back to Total Page
        time.sleep(0.5)
        browser.back()

        # Move to the next element
        if browser.find_element(By.XPATH, f'/html/body/div[3]/div[2]/table/tbody/tr[{current_element_number}]/td[9]').text == str('완료'):
            current_element_number += 2
        else:
            current_element_number += 1


def printbook():
    title = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[1]/strong').text
    print(title)

    if browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/th[1]').text == '강좌':
        lecture_str = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[1]').text
        # 부교재 확인하기
        if '워크북' in title or '시냅스' in title:
            print(lecture_str+' 의 부교재')
        else:
            print(lecture_str)
            
    elif browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/th[1]').text == '교재':
        book_str = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[3]/td[1]').text
        index = book_str.rfind('(') # Find the index of the last '(' in the string
        if index != -1:
            book_str = book_str[:index].rstrip() # Remove the text after the last '(' and any trailing whitespace
        
        print(book_str)

def function():
    goToTotalPage()

    #select book title
    select = Select(browser.find_element(By.ID, 'sel_chr_cd'))
    browser.implicitly_wait(10)
    time.sleep(1)
    select.select_by_visible_text('2024 현우진의 뉴런 - 수학l (공통)')


    browser.find_element(By.ID, 'searchSdt').clear()
    browser.find_element(By.ID, 'searchSdt').send_keys('2023-03-01')
    browser.implicitly_wait(10)   

    browser.find_element(By.ID, 'searchEdt').clear()
    browser.find_element(By.ID, 'searchEdt').send_keys('2023-03-02')
    browser.implicitly_wait(10)

    browser.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/a[1]').click()
    browser.implicitly_wait(10)

    paging(goingThroughTotalPage)


function()