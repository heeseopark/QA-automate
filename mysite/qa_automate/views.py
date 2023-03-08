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

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        element = BlacklistTest(student_name=student_name, student_id=student_id)
        element.save()
        return HttpResponseRedirect('/blacklist/')
