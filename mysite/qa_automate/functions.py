
from .models_v1 import BlackList, BookList, FaqAndEstimatedAnswer, SearchedQuestionList, ExtractedAndAnsweredQuestionList
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
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

### basic functions start ###

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

# paging 함수 맞게 작동하는지 체크해야함
def paging(function):
    while True:
        try:
            wait = WebDriverWait(browser, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/a[11]')))
            print('in page 1')
            function()
            for i in range(2, 11):
                browser.find_element(By.XPATH, f'/html/body/div[3]/div[3]/div/a[{i}]').click()
                browser.implicitly_wait(10)
                print(f'in page {i}')
                function()
            try:
                browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/a[11]').click()
                browser.implicitly_wait(10)
            except TimeoutException:
                return
        except TimeoutException:
            print('in page 1')
            function()
            page_number = 2
            while True:
                try:
                    wait = WebDriverWait(browser, 1)
                    wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div/a[{page_number}]'))).click()
                    browser.implicitly_wait(10)

                    # Check if next page is available
                    try:
                        browser.find_element(By.XPATH, f'/html/body/div[3]/div[3]/div/a[{page_number + 1}]')
                    except NoSuchElementException:
                        # If the next page is not available, execute the function and exit the loop
                        print(f'in page {page_number}')
                        function()
                        return

                except TimeoutException:
                    return

                else:
                    # Do something with current_element
                    print(f'in page {page_number}')
                    function()
                    page_number += 1

def getPageNum(text):
    patterns = [
        r'\b[pP](?:[gG])?\.?\s?(\d+)\s*',
        r'\b(\d+)\s?[pP](?:[gG]\.?)?\s*',
        r'\b(\d+)\s?(?:페|페이지|쪾|쪽)\s*',
        r'\b(?:페이지)\s?(\d+)\s*',
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            num_str = match.group(1)
            if num_str.strip() == '' or num_str.strip() != num_str:
                return 0
            return int(num_str)
    return 0

def getQuestionNum(text):
    patterns = [
        r'\b(\d+)\s?(?:번)\s*',
        r'\b(?:예제|문제)\s?(\d+)\s*',
        r'[#]\s?(\d+)\s*',
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            num_str = match.group(1)
            if num_str.strip() == '' or num_str.strip() != num_str:
                return 0
            return int(num_str)
    return 0

def getThemeNum(text):
    patterns = [
        r'\b(?:th|TH|Th|띰|theme|Theme)\s?(\d+)\s*',
        r'\b(\d+)\s?(?:th|TH|Th|띰|theme|Theme)\s*',
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            num_str = match.group(1)
            if num_str.strip() == '' or num_str.strip() != num_str:
                return 0
            return int(num_str)
    return 0

### basic functions end ###

### search functions start ###

def goingThroughTotalPageForSearch():

    current_element_number = 1

    while True:
        # Check if the current element is clickable
        try:
            wait = WebDriverWait(browser, 1)
            wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[2]/table/tbody/tr[{current_element_number}]/td[5]/a'))).click()
        except TimeoutException:
            break
                
        # Do something with the current element
        getAndSaveAtrributes()
        
        # Go Back to Total Page
        browser.back()

        # Move to the next element
        if browser.find_element(By.XPATH, f'/html/body/div[3]/div[2]/table/tbody/tr[{current_element_number}]/td[9]').text == str('완료'):
            current_element_number += 2
        else:
            current_element_number += 1

def getAndSaveAtrributes():
   
    # Get question title text
    title = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[1]/strong').text

    if browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/th[1]').text == '강좌':
        lecture_str = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[1]').text
        try:
            book = BookList.objects.get(lecture=lecture_str, type='주교재')
            # 부교재 확인하기
            if '워크북' in title or '시냅스' in title:
                book = BookList.objects.get(lecture=lecture_str, type='부교재')
        except BookList.DoesNotExist:
            return

    elif browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/th[1]').text == '교재':
        try:
            book_str = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[3]/td[1]').text
            index = book_str.rfind('(') # Find the index of the last '(' in the string
            if index != -1:
                book_str = book_str[:index].rstrip() # Remove the text after the last '(' and any trailing whitespace
            book = BookList.objects.get(title = book_str)

        except BookList.DoesNotExist:
            return

    # Get question_id
    question_id = int(browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[2]').text)
    
    # Get page, question, and theme numbers
    page_num = getPageNum(title)
    question_num = getQuestionNum(title)
    theme_num = getThemeNum(title)

    # Get question_date
    question_date = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[2]').text[:10]

    # Add question to SearchedQuestionList Table
    search = SearchedQuestionList(book = book, id = question_id, page = page_num, number = question_num, theme = theme_num, date = question_date)
    search.save()

    # Check if sum of boolean values is less than 2
    if not (bool(page_num) or bool(question_num)):
        return

    # Check if question attribute already exists in FAQListAndEstimatedAnswer table
    try:
        faq = FaqAndEstimatedAnswer.objects.get(book=book, page=page_num, number=question_num, theme=theme_num )
        faq.count += 1
        faq.save()
    except FaqAndEstimatedAnswer.DoesNotExist:
        # If question attribute does not exist, create a new one
        faq = FaqAndEstimatedAnswer.objects.create(book=book, page=page_num, number=question_num, theme=theme_num, count=1)
    
def updateSearchedAndFaqTable(start_text, end_text, title_text):

    goToTotalPage()
   
    #select book title
    select = Select(browser.find_element(By.ID, 'sel_chr_cd'))
    browser.implicitly_wait(10)
    time.sleep(1)
    select.select_by_visible_text(title_text)

    browser.find_element(By.ID, 'searchSdt').clear()
    browser.find_element(By.ID, 'searchSdt').send_keys(start_text)
    browser.implicitly_wait(10)   

    browser.find_element(By.ID, 'searchEdt').clear()
    browser.find_element(By.ID, 'searchEdt').send_keys(end_text)
    browser.implicitly_wait(10)

    browser.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/a[1]').click()
    browser.implicitly_wait(10)
    
    paging(goingThroughTotalPageForSearch)

    browser.quit()

def getqas(date, ids):
    default_text = """
============================================
클린 학습 Q&A 게시판 우선 검색하셨나요?
클린 학습 Q&A 게시판/ 인터넷 검색엔진으로
얻을 수 있는 질문에는 답변이 제한됩니다.
같은 질문들이 아주 많다는 점 먼저 참고하신 후 이용해 주세요!

0. 질문 제목글에는 아래 1번 또는 2번 내용을 적어주세요.
1. (교재명) 교재 페이지, 문항 번호
2. (강좌명) 강의 시간대
3. 문의 내용
4. 문의 내용에 대한 학생이 생각하는 근거
============================================

1.
2.
3.
4.


[참고]
- 본인의 풀이 방법에 대한 확인 요청일 경우 본인 풀이 과정 반드시 첨부할 것!
- 문제의 전체 풀이 또는 다른 풀이는 진행해주지 않음(ex. 이 문제 경우의 수로 풀어주세요.)
- 단순 계산 및 교과서에 포함되지 않은 증명, 그래프 그리기 등은 답변하지 않음(ex. 미적분의 기본원리 증명해 주세요.)
- 중학 수학 등 이미 학습이 완료되어 있어야 할 부분에 대한 원리, 증명, 공식 등에 대한 설명은 하지 않음 (ex. 이차함수의 축을 어떻게 구하나요?)
    """
    goToTotalPage()

    browser.find_element(By.ID, 'searchSdt').clear()
    browser.find_element(By.ID, 'searchSdt').send_keys(date)
    browser.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/a[1]').click()
    browser.implicitly_wait(10)

    qalist = []
    for id in ids:
        select = Select(browser.find_element(By.ID, 'smode'))
        browser.implicitly_wait(10)
        select.select_by_visible_text('고유번호')
        browser.find_element(By.ID, 'sword').clear()
        browser.find_element(By.ID, 'sword').send_keys(id)
        browser.implicitly_wait(10)
        browser.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/a[1]').click()
        
        browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[1]/td[5]/a').click()

        question_text = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[5]/td').text
        default_text_lines = default_text.split("\n")
        question_text_lines = question_text.split("\n")

        # Initialize an empty string for the extracted text
        extracted_text = ""

        # Iterate over each line in the question text
        for i in range(len(question_text_lines)):
            # If the line is not in the default text, add it to the extracted text
            if question_text_lines[i] not in default_text_lines:
                if question_text_lines[i] == '============================================':
                    continue
                extracted_text += question_text_lines[i] + "\n"
        
        # Get answer text
        try:
            answer_text = browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[4]/td').text
        except NoSuchElementException:
            answer_text = '답변 없음'


        qalist.append((extracted_text, answer_text))

        browser.back()

    return qalist

        






### search functions end ###



### extract and answer functions start ###


def goingThroughWaitingPageForExtract():

    current_element_number = 1

    while True:
        try:
            browser.implicitly_wait(10)
            time.sleep(1)
            element = browser.find_element(By.XPATH, f'/html/body/div[3]/div[2]/table/tbody/tr[{current_element_number}]/td[5]/a')
            if element.is_displayed():
                element.click()
        except NoSuchElementException:
            break
        except ElementClickInterceptedException:
            current_element_number += 1
            continue

        # Do something with the current element
        checkFaq()

        # Go back to waiting page
        browser.back()

        # Move to the next element
        current_element_number += 1

def checkFaq():
    # Get question title text
    title = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[1]/strong').text
    # global book

    if browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/th[1]').text == '강좌':
        lecture_str = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[1]').text
        try:
            book = BookList.objects.get(lecture=lecture_str, type='주교재')
            # 부교재 확인하기
            if '워크북' in title or '시냅스' in title:
                book = BookList.objects.get(lecture=lecture_str, type='부교재')
        except BookList.DoesNotExist:
            return

    elif browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/th[1]').text == '교재':
        try:
            book_str = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[3]/td[1]').text
            index = book_str.rfind('(') # Find the index of the last '(' in the string
            if index != -1:
                book_str = book_str[:index].rstrip() # Remove the text after the last '(' and any trailing whitespace
            book = BookList.objects.get(title = book_str)

        except BookList.DoesNotExist:
            return
    
    # Get question_id
    question_id = int(browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[2]').text)

    # Get page, question, and theme numbers
    page_num = getPageNum(title)
    question_num = getQuestionNum(title)
    theme_num = getThemeNum(title)
    # Get student name and id 
    student_name_and_id = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[4]/td[1]/a').text

    # 교재 없는 경우 그냥 빈 return 던지기
    book_purchase = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[4]/td[3]').text
    if book_purchase == 'N':
        return
    
    book_purchase_2 = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[4]/td[4]/a').text
    if 'N' in book_purchase_2:
        return    
    
    # 학생 이름, id blakclist에 있는 경우에도 그냥 빈 return 던지기 (strip해서 앞 뒤로 빈칸 없게)
    if student_name_and_id in BlackList.objects.all():
        print(f'{question_id} 학생 답변 금지 목록에 있어 제외됨')
        return
    

    # 키워드 있는지 확인과정, 밑에 for loop에서 priority 계산
    if FaqAndEstimatedAnswer.objects.filter(book=book, page=page_num, number=question_num, theme=theme_num).exists():
        keywords_text = FaqAndEstimatedAnswer.objects.get(book=book, page=page_num, number=question_num, theme=theme_num).keywords

    if page_num == 0 or question_num == 0:
        return


    
    keywords_list = str(keywords_text).strip().split(',')

    # Get question text and calculate priority
    question_text = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[5]/td').text
    priority = 0
    for keyword in keywords_list:
        if keyword in question_text:
            priority += 1

    estimated_answer = str(FaqAndEstimatedAnswer.objects.get(book=book, page=page_num, number=question_num, theme=theme_num).answer)

    question_obj = ExtractedAndAnsweredQuestionList(id = question_id, book = book, student = student_name_and_id, page = page_num, number = question_num, theme = theme_num, question = question_text, answer = estimated_answer, done = False, priority = priority)
    question_obj.save()

def extractquestions():
    goToWaitingPage()

    paging(goingThroughWaitingPageForExtract)

def answer():
    goToWaitingPage()


    for question in ExtractedAndAnsweredQuestionList.objects.filter(done=False):
        id = question.id


        select = Select(browser.find_element(By.ID, 'smode'))
        browser.implicitly_wait(10)
        select.select_by_visible_text('고유번호')

        browser.find_element(By.ID, 'sword').send_keys(id)
        browser.implicitly_wait(10)

        #이미 답변이 되어서 질문이 없는 경우에 다음 질문 넘어가면서 db 내 질문도 같이 삭제
        try:
            wait = WebDriverWait(browser, 1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[1]/td[5]/a'))).click()
        except TimeoutException:
            question.delete()
            continue
        
        #다른 사람이 찜한 경우에 다음 질문 넘어가면서 db 내 질문도 같이 삭제
        try:
            wait = WebDriverWait(browser, 1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/a[1]'))).click()
        except TimeoutException:
            try:
                # Wait for the alert to appear and switch to it
                WebDriverWait(browser, 1).until(EC.alert_is_present())

                # If the alert is present, accept it
                alert = browser.switch_to.alert
                alert.accept()

                # Switch back to the main window
                browser.switch_to.default_content()

            except TimeoutException:
                pass

            question.delete()
            browser.back()
            continue

        #go into iframe
        wait = WebDriverWait(browser, 2)
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

        # Switch to the iframe element
        browser.switch_to.frame(iframe)

        wait = WebDriverWait(browser, 2)
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

        # Switch to the 2nd iframe element
        browser.switch_to.frame(iframe)

        answertextarea = browser.find_element(By.XPATH, '/html/body')
        estimatedanswer = question.answer

        answertextarea.send_keys(estimatedanswer)

        browser.switch_to.default_content()

        browser.switch_to.default_content()

        answerbutton = browser.find_element(By.XPATH, '//*[@id="reg_area"]/a[1]')

        answerbutton.click()

        # Switch to the alert
        alert = browser.switch_to.alert

        # Accept the alert by pressing ENTER
        alert.accept()

        # Switch back to the main window
        browser.switch_to.default_content()
        
        question.done = True
        question.save()

### extract and answer functions end ###


### functions for writing estimated answer ###
# gp4 결과 그냥 가져온거이기 때문에 확인해봐야함

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from openai import OpenAI

def cluster_qapairs(qa_pairs):

    # Convert qa_pairs to a list of dictionaries to maintain compatibility with the remaining code
    qa_pairs = [{"question": pair[0], "answer": pair[1]} for pair in qa_pairs]

    # 1. Extract keywords (simplified using TF-IDF)
    vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000, min_df=2, stop_words='english', use_idf=True)
    X = vectorizer.fit_transform([" ".join(pair.values()) for pair in qa_pairs])

    # 2. Cluster Q&A pairs (using K-means)
    km_model = KMeans(n_clusters=5)
    km_model.fit(X)

    clusters = km_model.labels_.tolist()

    # 3. Organize Q&A pairs into clusters
    clustered_qa_pairs = {i: [] for i in range(5)}
    for i, cluster in enumerate(clusters):
        clustered_qa_pairs[cluster].append(qa_pairs[i])

    # 4. Generate estimated answers
    openai = OpenAI("your-api-key")
    estimated_answers = {}

    for cluster, pairs in clustered_qa_pairs.items():
        prompt = ""
        for pair in pairs:
            prompt += f"Question: {pair['question']}\nAnswer: {pair['answer']}\n"

        response = openai.Completion.create(
        model="gpt-4.0-turbo",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
        )

        estimated_answers[cluster] = response.choices[0].text.strip()

    # 5. Return top 5 classification cases
    # Assuming 'top' means 'most Q&A pairs'
    top_clusters = sorted(clustered_qa_pairs.items(), key=lambda x: len(x[1]), reverse=True)[:5]
    result = []

    for cluster, pairs in top_clusters:
        print(f"Cluster: {cluster}, Keywords: {vectorizer.get_feature_names()}, Estimated answer: {estimated_answers[cluster]}")
        # Convert pairs back to the original format and add to the result
        result.extend([[pair["question"], pair["answer"]] for pair in pairs])

    return result


