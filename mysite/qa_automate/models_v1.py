from django.db import models

# Create your models here.

class BlackList(models.Model): #답변 금지 학생 목록
    student = models.CharField(max_length=50, primary_key=True)

class BookList(models.Model): #새 교재 나올 때 마다 추가
    lecture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=10, default='주교재')


class DateCheck(models.Model): #각 교재별로 조사한 날짜들 저장
    book = models.ForeignKey(BookList, on_delete=models.CASCADE, to_field='title')
    date = models.DateField(null=True)

class SearchedQuestionList(models.Model): #모든 교재에 대해 조사한 질문들 저장
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookList, on_delete=models.CASCADE, to_field='title')
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    date = models.DateField()
    #img = models.ImageField()

class FaqAndEstimatedAnswer(models.Model): #FAQ와 예상 답변 저장
    book = models.ForeignKey(BookList, on_delete=models.CASCADE, to_field='title')
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    count = models.IntegerField(default=1)
    keywords = models.CharField(max_length=200, null=True)
    answer = models.TextField(default='') 

class ExtractedAndAnsweredQuestionList(models.Model): #추출한 모든 답변 가능 질문들 저장
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookList, on_delete=models.CASCADE, to_field='title')
    student = models.CharField(max_length=50)
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    question = models.TextField()
    answer = models.TextField()
    done = models.BooleanField()
    priority = models.IntegerField(default=0)
    #img = models.ImageField()

class Extractforview(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(default='')
    book = models.ForeignKey(BookList, on_delete=models.CASCADE, to_field='title')
    student = models.CharField(max_length=50)
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    question = models.TextField()
    #img = models.ImageField()