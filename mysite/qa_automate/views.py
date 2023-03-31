from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BookListTest, BlacklistTest, DateCheckTest, FaqAndEstimatedAnswerTest, SearchedQuestionListTest
from .functions import isInBlackList, goToWaitingPage, updateSearchedAndFaqTable, goToTotalPage
from datetime import datetime, timedelta

# Create your views here.

def init(request):
    return render(request, 'qa_automate/init.html')

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
        booktype = request.POST.get('book_type')
        book = BookListTest(title=title, lecture=lecture, book_type = booktype)
        book.save()
        return HttpResponseRedirect('/qa_automate/booklist/')
    
    context = {
        'books': books,
    }
    
    return render(request, 'qa_automate/booklist.html', context)



def calender(request, book_title):
    book = BookListTest.objects.get(title=book_title)
    date_checks = DateCheckTest.objects.filter(book=book)

    # Get a list of years for which there are searched dates
    searched_years = set(date_check.year for date_check in date_checks)
    searched_months = set(i for i in range(1,13))

    if request.method == 'POST':
        startdate_str = request.POST.get('startdate')
        enddate_str = request.POST.get('enddate')
        startdate = datetime.strptime(startdate_str, '%Y-%m-%d').date()
        enddate = datetime.strptime(enddate_str, '%Y-%m-%d').date()

        # DateCheck DB 업데이트
        current_date = startdate
        while current_date <= enddate:
            if not DateCheckTest.objects.filter(book=book, year=current_date.year, month=current_date.month, date=current_date.date).exists():
                date_check = DateCheckTest(book=book, year=current_date.year, month=current_date.month, date=current_date.date)
                date_check.save()
            current_date += timedelta(days=1)

        # Searched DB, FaQ DB 업데이트
        updateSearchedAndFaqTable(startdate_str, enddate_str, book.title)
        return HttpResponseRedirect(reverse('qa_automate:calender', args=[book.title]))

    # Get a list of dates for which there are searched dates
    searched_dates = [[date_check.year, date_check.month, date_check.date] for date_check in date_checks]

    context = {
        'book': book_title,
        'searched_dates': searched_dates,
        'searched_months': searched_months,
        'searched_years': searched_years,
    }
    return render(request, 'qa_automate/calender.html', context)


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
