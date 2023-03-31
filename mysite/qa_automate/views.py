from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BookListTest, BlacklistTest, DateCheckTest, FaqAndEstimatedAnswerTest, SearchedQuestionListTest
from .functions import isInBlackList, goToWaitingPage, updateSearchedAndFaqTable, goToTotalPage
import datetime

# Create your views here.

def init(request):
    return render(request, 'qa_automate/init.html')

def calender(request, book_title):
    book = BookListTest.objects.get(title=book_title)
    dates = DateCheckTest.objects.filter(book=book)

    # Get a list of years for which there are searched dates
    searched_years = set(date.year for date in dates)

    if request.method == 'POST':
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        current_date = startdate

        #DateCheck DB 업데이트
        while current_date <= enddate:
            date_obj = datetime.datetime.strptime(current_date, '%Y-%m-%d').date()
            if DateCheckTest.objects.filter(book=book, date=date_obj).exists():
                pass
            else:
                date_check = DateCheckTest(book=book, date=date_obj)
                date_check.save()
            current_date = (datetime.datetime.strptime(current_date, '%Y-%m-%d') + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        
        #Searched DB, FaQ DB 업데이트 
        updateSearchedAndFaqTable(str(startdate), str(enddate), str(book_title))   
        return HttpResponseRedirect(reverse('qa_automate:calender', args=[book_title]))

    # Get a list of dates for which there are searched dates
    searched_dates = [date.date for date in dates]

    context = {
        'book': book_title,
        'dates': dates,
        'searched_dates': searched_dates,
        'searched_years': searched_years,
    }
    return render(request, 'qa_automate/calender.html', context)

def booklist(request):
    books = BookListTest.objects.all().order_by('lecture', 'title')

    if request.method == 'POST' and 'delete_book' in request.POST:
        title = request.POST.get('delete_book')
        book = BookListTest.objects.filter(title=title).first()
        if book:
            book.delete()
    elif request.method == 'POST':
        title = request.POST.get('title')
        lecture = request.POST.get('lecture')
        book = BookListTest(title=title, lecture=lecture)
        book.save()
    return render(request, 'qa_automate/booklist.html', {'books': books})


def blacklist(request):
    elements = BlacklistTest.objects.all()
    if request.method == 'POST':
        student_name_and_id = request.POST.get('student_name_and_id')
        element = BlacklistTest(student_name_and_id=student_name_and_id)
        element.save()
        return HttpResponseRedirect('/qa_automate/blacklist/')
    return render(request, 'qa_automate/blacklist.html', {'elements': elements})

def faqlist(request):
    books = FaqAndEstimatedAnswerTest.objects.values_list('book__title', flat=True).distinct()
    selected_book = request.GET.get('book')
    if selected_book:
        unanswerable_questions = FaqAndEstimatedAnswerTest.objects.filter(answer='', book__title=selected_book)
        answerable_questions = FaqAndEstimatedAnswerTest.objects.exclude(answer='', book__title=selected_book)
    else:
        unanswerable_questions = FaqAndEstimatedAnswerTest.objects.filter(answer='')
        answerable_questions = FaqAndEstimatedAnswerTest.objects.exclude(answer='')
    context = {
        'unanswerable_questions': unanswerable_questions,
        'answerable_questions': answerable_questions,
        'books': books,
    }
    return render(request, 'qa_automate/faqlist.html', context)

def estimatedanswer(request, book_title, page, theme, number):
    # Get the matching question object
    question = SearchedQuestionListTest.objects.get(
        book__title=book_title, page=page, theme=theme, number=number)

    # Check if there's already an estimated answer for the question
    try:
        faq = FaqAndEstimatedAnswerTest.objects.get(
            book__title=book_title, page=page, theme=theme, number=number)
        answer = faq.answer
    except FaqAndEstimatedAnswerTest.DoesNotExist:
        answer = ''

    if request.method == 'POST':
        answer = request.POST['answer']

        # Check if there's already an estimated answer for the question
        try:
            faq = FaqAndEstimatedAnswerTest.objects.get(
                book__title=book_title, page=page, theme=theme, number=number)
            faq.answer = answer
            faq.save()
        except FaqAndEstimatedAnswerTest.DoesNotExist:
            book = BookListTest.objects.get(title=book_title)
            faq = FaqAndEstimatedAnswerTest(
                book=book, page=page, theme=theme, number=number, answer=answer)
            faq.save()

    return render(request, 'qa_automate/estimatedanswer.html', {'question': question, 'answer': answer})


def test(request):
    return render(request, 'qa_automate/estimatedanswer.html')

def extract(request):
    return render(request, 'qa_automate/extract.html')

def searched(request, book_title):
    questions = SearchedQuestionListTest.objects.filter(book=book_title)
    if request.method == 'GET':
        page_num = request.GET.get('page_num')
        theme_num = request.GET.get('theme_num')
        question_num = request.GET.get('question_num')
        if page_num:
            questions = questions.filter(page=page_num)
        if theme_num:
            questions = questions.filter(theme=theme_num)
        if question_num:
            questions = questions.filter(number=question_num)
    return render(request, 'qa_automate/searchedlist.html', {'questions': questions, 'book': book_title})
