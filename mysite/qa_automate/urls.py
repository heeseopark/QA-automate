from django.urls import path
from . import views

app_name = 'qa_automate'

urlpatterns = [
    path('', views.init, name='init'),
    path('calender/<str:book_title>', views.calender, name='calender'),
    path('booklist/', views.booklist),
    path('blacklist/', views.blacklist),
    path('test/', views.test),
    path('faqlist/', views.faqlist, name='faq_list'),
    path('estimated_answer/<str:book_title>/<int:page>/<int:theme>/<int:number>/', views.estimatedanswer, name='estimated_answer'),
]

