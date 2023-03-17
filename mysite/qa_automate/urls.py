from django.urls import path
from . import views
from selenium import webdriver

app_name = 'qa_automate'

urlpatterns = [
    path('', views.init),
    path('calender/', views.calender),
    path('booklist/', views.add_book_list),
    path('blacklist/', views.blacklist),
    path('search/', views.search_date),
]

