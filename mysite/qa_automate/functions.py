from .models import BlacklistTest, BookListTest, FaqListTest
import time
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def isInBlackList(text):
    """
    Checks whether the given name and id exist in the BlacklistTest table.
    Returns True if the student is in the blacklist, False otherwise.
    """
    try:
        blacklist = BlacklistTest.objects.get(student_name_and_id=text)
        return True
    except BlacklistTest.DoesNotExist:
        return False
    
def goToWaitingPage():

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

def goToTotalPage():
    
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

def paging(browser, function):
    # Define a function to check if a JavaScript function exists on the page
    def isExecutable(function_name):
        script = f"return typeof {function_name} === 'function';"
        result = browser.execute_script(script)
        return result

    # Loop through the JavaScript functions until we reach the last page
    current_page = 1
    while True:
        # Check if the current function is executable
        function_name = f"goPage({current_page})"
        if not isExecutable(function_name):
            break

        # Execute the JavaScript function
        browser.execute_script(f"javascript:{function_name}")

        # Do something with the current page
        function

        current_page += 1


def getQuestionAttribute(browser):
    # Switch to iframe
    iframe = browser.find_element(By.TAG_NAME,"iframe")
    browser.switch_to.frame(iframe)

    # Check if we need to go to previous page
    if browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[4]/td[3]').text == 'N':
        browser.switch_to.default_content()
        # Go to previous page
        browser.back()
        return

    # Get question ID
    question_id = int(browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[2]').text)

    # Get Student name and ID
    student_name_and_id = browser.find_element(By.XPATH, "/html/body/div[1]/table/tbody/tr[4]/td[1]/a").text

    # Get book object
    book_title = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[1]').text
    book = BookListTest.objects.get(title=book_title)

    # Get Page Number and Question Number
    text = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[1]/strong').text
    page_number = getPageNum(text)
    question_number = getQuestionNum(text)
    theme_number = getThemeNum(text)

    # Save question attributes to database
    question = FaqListTest(
        
        question_id=question_id,
        book=book,
        student_name_and_id=student_name_and_id,  # TODO: Replace with actual student name
        page=page_number,  # TODO: Replace with actual page number
        number=question_number,  # TODO: Replace with actual question number
        theme=theme_number,  # TODO: Replace with actual theme number

    )
    question.save()

    # Switch back to default content and go to previous page
    browser.switch_to.default_content()
    browser.back()

def getPageNum(text):
    pattern = r'(?:\b\d+\s*)?(?:p(?:g)?\.?\s{0,2})*(\d+)(?:[페페이지쪽]|\s*$)'
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        return None


def getQuestionNum(text):
    pattern = r'(?:^|[^0-9])(\d{1,2})\s*[번]'
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        return None

def getThemeNum(text):
    pattern = r'(?:^|[^0-9])(\d{1,2})\s*(?:띰|theme)'
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        return None

def inputDateAndUpdateTable(start_text, end_text, title_text):

    goToTotalPage()

    time.sleep(3)

    # Switch to iframe   
    service = Service('.\chromedriver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(service=service, options=options)
   
    # Wait for the iframe element to become available
    wait = WebDriverWait(browser, 10)
    iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

    # Switch to the iframe element
    browser.switch_to.frame(iframe)
    browser.implicitly_wait(10)

    #select book title
    select = Select(browser.find_element(By.ID, 'sel_chr_cd'))
    browser.implicitly_wait(10)

    select.select_by_value(title_text)
    browser.implicitly_wait(10)

    browser.switch_to.frame(iframe)

    browser.find_element(By.ID, 'searchSdt').send_keys(start_text)
    browser.implicitly_wait(10)   

    browser.find_element(By.ID, 'searchEdt').send_keys(end_text)
    browser.implicitly_wait(10)

    browser.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/a[1]').click()
    browser.implicitly_wait(10)

    paging(browser, None)



