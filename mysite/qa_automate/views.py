from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


# Create your views here.


def init(request):
    return render(request, 'qa_automate/init.html')


def calender(request):
    return render(request, 'qa_automate/datepicker.html')



#/

