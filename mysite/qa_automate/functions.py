from .models import BlacklistTest, BookListTest, QuestionListTest
import time
from selenium import webdriver

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
    
def goToWaitingPage(browser):
    # navigate to the website
    browser.get('https://www.tzonemegastudy.net/')

    # find and click the first element
    first_element = browser.find_element_by_xpath('/html/body/form/div/div[1]/label[2]/input')
    first_element.click()

    # find and input text into the second element
    second_element = browser.find_element_by_id('id')
    second_element.send_keys('heeseopark')

    # find and click the third element
    third_element = browser.find_element_by_id('sp_smsct')
    third_element.click()

    # find and input text into the fourth element
    fourth_element = browser.find_element_by_id('second_tec_cd')
    fourth_element.send_keys('heeseo1099')

    # find and click the fifth element
    fifth_element = browser.find_element_by_id('sp_login')
    fifth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the sixth element
    sixth_element = browser.find_element_by_id('a594')
    sixth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the seventh element
    seventh_element = browser.find_element_by_id('aa4233')
    seventh_element.click()

def goToTotalPage(browser):
    # navigate to the website
    browser.get('https://www.example.com/')

    # find and click the first element
    first_element = browser.find_element_by_xpath('/html/body/form/div/div[1]/label[2]/input')
    first_element.click()

    # find and input text into the second element
    second_element = browser.find_element_by_id('id')
    second_element.send_keys('heeseopark')

    # find and click the third element
    third_element = browser.find_element_by_id('sp_smsct')
    third_element.click()

    # find and input text into the fourth element
    fourth_element = browser.find_element_by_id('second_tec_cd')
    fourth_element.send_keys('heeseo1099')

    # find and click the fifth element
    fifth_element = browser.find_element_by_id('sp_login')
    fifth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the sixth element
    sixth_element = browser.find_element_by_id('a594')
    sixth_element.click()

    # wait for 3 seconds
    time.sleep(3)

    # find and click the seventh element
    seventh_element = browser.find_element_by_id('aa4231')
    seventh_element.click()

def paging(browser):
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
        getQuestionAttribute(browser)

        current_page += 1


def getQuestionAttribute(browser):
    # Switch to iframe
    iframe = browser.find_element_by_tag_name("iframe")
    browser.switch_to.frame(iframe)

    # Check if we need to go to previous page
    if browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[4]/td[3]').text == 'N':
        browser.switch_to.default_content()
        # Go to previous page
        browser.back()
        return

    # Get question ID
    question_id = int(browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]').text)

    # Get Student name and ID
    student_name_and_id = browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[4]/td[1]/a").text

    # Get book object
    book_title = browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[1]').text
    book = BookListTest.objects.get(title=book_title)

    # Save question attributes to database
    question = QuestionListTest(
        question_id=question_id,
        book=book,
        question_number=1,  # TODO: Replace with actual question number
        student_name_and_id=student_name_and_id,  # TODO: Replace with actual student name
        page=1,  # TODO: Replace with actual page number
        number=1,  # TODO: Replace with actual question number
        theme=1,  # TODO: Replace with actual theme number
        example=1  # TODO: Replace with actual example number
    )
    question.save()

    # Switch back to default content and go to previous page
    browser.switch_to.default_content()
    browser.back()
