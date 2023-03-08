from .models import BlacklistTest

def isInBlackList(name, id):
    """
    Checks whether the given name and id exist in the BlacklistTest table.
    Returns True if the student is in the blacklist, False otherwise.
    """
    try:
        blacklist = BlacklistTest.objects.get(student_name=name, student_id=id)
        return True
    except BlacklistTest.DoesNotExist:
        return False


def isInQuestionList():
    pass


import time
from selenium import webdriver

def goToWaitingPage():
    # set up the Chrome driver
    driver = webdriver.Chrome()

    # navigate to the website
    driver.get('https://www.example.com/')

    # find and click the first element
    first_element = driver.find_element_by_xpath('/html/body/form/div/div[1]/label[2]/input')
    first_element.click()

    # find and input text into the second element
    second_element = driver.find_element_by_id('id')
    second_element.send_keys('heeseopark')

    # find and click the third element
    third_element = driver.find_element_by_id('sp_smsct')
    third_element.click()

    # find and input text into the fourth element
    fourth_element = driver.find_element_by_id('second_tec_cd')
    fourth_element.send_keys('heeseo1099')

    # find and click the fifth element
    fifth_element = driver.find_element_by_id('sp_login')
    fifth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the sixth element
    sixth_element = driver.find_element_by_id('a594')
    sixth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the seventh element
    seventh_element = driver.find_element_by_id('aa4233')
    seventh_element.click()


def goToTotalPage():
    # set up the Chrome driver
    driver = webdriver.Chrome()

    # navigate to the website
    driver.get('https://www.example.com/')

    # find and click the first element
    first_element = driver.find_element_by_xpath('/html/body/form/div/div[1]/label[2]/input')
    first_element.click()

    # find and input text into the second element
    second_element = driver.find_element_by_id('id')
    second_element.send_keys('heeseopark')

    # find and click the third element
    third_element = driver.find_element_by_id('sp_smsct')
    third_element.click()

    # find and input text into the fourth element
    fourth_element = driver.find_element_by_id('second_tec_cd')
    fourth_element.send_keys('heeseo1099')

    # find and click the fifth element
    fifth_element = driver.find_element_by_id('sp_login')
    fifth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the sixth element
    sixth_element = driver.find_element_by_id('a594')
    sixth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the seventh element
    seventh_element = driver.find_element_by_id('aa4231')
    seventh_element.click()

