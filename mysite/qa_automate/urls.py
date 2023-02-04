from django.urls import path
from . import views

urlpatterns = [
    path('', views.init),
    path('<int:question_id>/', views.detail, name='detail'),
    path('ex/', views.index, name='index'),
    path('calender/', views.calender)
]