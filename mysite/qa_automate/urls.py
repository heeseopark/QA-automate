from django.urls import path
from . import views

app_name = 'qa_automate'

urlpatterns = [
    path('', views.init),
    path('calender/', views.calender),
    path('booklist/', views.searchQuestion),
    path('blacklist/', views.blacklist),
    path('search/', views.searchDate),
    path('test/', views.test),
    path('faqlist/', views.faqList),
]

