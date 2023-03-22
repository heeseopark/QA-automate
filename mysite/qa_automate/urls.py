from django.urls import path
from . import views

app_name = 'qa_automate'

urlpatterns = [
    path('', views.init, name = 'init'),
    path('calender/<str:book_title>/', views.calender, name = 'calender'),
    path('booklist/', views.booklist),
    path('blacklist/', views.blacklist),
    path('search/', views.searchDate),
    path('test/', views.test),
    path('faqlist/', views.faqList),
]

