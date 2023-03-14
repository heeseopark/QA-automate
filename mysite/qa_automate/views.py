from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import BookListTest
from .models import BlacklistTest
# Create your views here.


def init(request):
    return render(request, 'qa_automate/init.html')


def calender(request):
    return render(request, 'qa_automate/datepicker.html')
    
def book_list(request):
    books = BookListTest.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        book = BookListTest(title=title)
        book.save()
        return HttpResponseRedirect('/')

    return render(request, 'book_list.html', {'books': books})

def blacklist(request):
    elements = BlacklistTest.objects.all()

    if request.method == 'POST':
        student_name_and_id = request.POST.get('student_name_and_id')
        element = BlacklistTest(student_name_and_id=student_name_and_id)
        element.save()
        return HttpResponseRedirect('/blacklist/')

    return render(request, 'blacklist.html', {'elements': elements})
