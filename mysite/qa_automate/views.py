from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import BookListTest
from .models import BlacklistTest

# Create your views here.

def init(request):
    return render(request, 'qa_automate/init.html')

def calender(request):
    if request.method == 'POST':
        return HttpResponseRedirect(request.get_full_path())

    return render(request, 'qa_automate/datepicker.html')
    
def add_book_list(request):

    books = BookListTest.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        book = BookListTest(title=title)
        book.save()
        return HttpResponseRedirect(request.get_full_path())

    return render(request, 'qa_automate/book_list.html', {'books': books})

def blacklist(request):
    elements = BlacklistTest.objects.all()

    if request.method == 'POST':
        student_name_and_id = request.POST.get('student_name_and_id')
        element = BlacklistTest(student_name_and_id=student_name_and_id)
        element.save()
        return HttpResponseRedirect('qa_automate/blacklist/')

    return render(request, 'qa_automate/blacklist.html', {'elements': elements})
