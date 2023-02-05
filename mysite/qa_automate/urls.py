from django.urls import path
from . import views

app_name = 'qa_automate'

urlpatterns = [
    path('', views.init),
    path('<int:question_id>/', views.detail, name='detail'),
    path('ex/', views.index, name='index'),
    path('calender/', views.calender),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]