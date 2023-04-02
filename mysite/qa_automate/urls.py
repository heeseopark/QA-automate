from django.urls import path
from . import views

app_name = 'qa_automate'

urlpatterns = [
    path('', views.init, name='init'),
    path('calender/<str:book_title>', views.calendar, name='calendar'),
    path('booklist/', views.booklist),
    path('blacklist/', views.blacklist),
    path('test/', views.test),
    path('faqlist/', views.faqlist, name='faq_list'),
    path('extract/', views.extract),
    path('estimated_answer/<str:book_title>/<int:page>/<int:theme>/<int:number>/', views.estimatedanswer, name='estimated_answer'),
    path('searched/<str:book_title>', views.searched, name='searched'),
    
]

