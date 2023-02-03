from django.urls import path
from . import views

urlpatterns = [
    path('', views.init),
    path('<int:question_id>/', views.detail),
]