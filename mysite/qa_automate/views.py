from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import BookTest
from .models import BlacklistTest
# Create your views here.


def init(request):
    return render(request, 'qa_automate/init.html')


def calender(request):
    return render(request, 'qa_automate/datepicker.html')

def book_list(request):
    books = BookTest.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        book = BookTest(title=title)
        book.save()
        return HttpResponseRedirect('/')

    return render(request, 'book_list.html', {'books': books})

def blacklist(request):
    elements = BlacklistTest.objects.all()

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        element = BlacklistTest(student_name=student_name, student_id=student_id)
        element.save()
        return HttpResponseRedirect('/blacklist/')

    return render(request, 'blacklist.html', {'elements': elements})

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
