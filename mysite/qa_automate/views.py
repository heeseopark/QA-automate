from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BookListTest, BlacklistTest, DateCheckTest, FaqAndEstimatedAnswerTest
from .functions import isInBlackList, goToWaitingPage, inputDateAndUpdateTable, goToTotalPage
import datetime

# Create your views here.

def init(request):
    return render(request, 'qa_automate/init.html')

def calender(request, book_title):
    book = BookListTest.objects.get(title=book_title)
    dates = DateCheckTest.objects.filter(book=book)
    if request.method == 'POST':
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        current_date = startdate
        while current_date <= enddate:
            date_obj = datetime.datetime.strptime(current_date, '%Y-%m-%d').date()
            if DateCheckTest.objects.filter(book=book, date=date_obj).exists():
                pass
            else:
                date_check = DateCheckTest(book=book, date=date_obj)
                date_check.save()
            current_date = (datetime.datetime.strptime(current_date, '%Y-%m-%d') + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        inputDateAndUpdateTable(str(startdate), str(enddate), str(book_title))
        return HttpResponseRedirect(reverse('qa_automate:calender', args=[book_title]))
    return render(request, 'qa_automate/calender.html', {'book_title': book_title, 'dates': dates})

def booklist(request):
    books = BookListTest.objects.all().order_by('title')
    if request.method == 'POST':
        title = request.POST.get('title')
        book = BookListTest(title=title)
        book.save()
    return render(request, 'qa_automate/book_list.html', {'books': books})

def blacklist(request):
    elements = BlacklistTest.objects.all()
    if request.method == 'POST':
        student_name_and_id = request.POST.get('student_name_and_id')
        element = BlacklistTest(student_name_and_id=student_name_and_id)
        element.save()
        return HttpResponseRedirect('/qa_automate/blacklist/')
    return render(request, 'qa_automate/blacklist.html', {'elements': elements})

def search_date(request):
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        selected_date = request.POST.get('selected_date')
        book = BookListTest.objects.get(title=book_title)
        date_obj = datetime.datetime.strptime(selected_date, '%Y-%m-%d').date()
        if DateCheckTest.objects.filter(book=book, date=date_obj).exists():
            searched = True
        else:
            searched = False
        return render(request, 'qa_automate/datepicker.html', {'book_title': book_title, 'selected_date': selected_date, 'searched': searched})
    else:
        return HttpResponseRedirect('/qa_automate/calender/')

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


def estimatedanswer(request):
    return render(request, 'qa_automate/estimatedanswer.html')

def test(request):
    return render(request, 'qa_automate/estimatedanswer.html')