from django.urls import path
from . import views

app_name = 'qa_automate'

urlpatterns = [
    path('', views.init),
    path('calender/', views.calender),
]