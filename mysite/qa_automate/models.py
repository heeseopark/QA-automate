from django.db import models

# Create your models here.

class BookListTest(models.Model): #새 교재 나올 때 마다 추가
    lecture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=10, default='주교재')

# 교재 와 강좌에 따른 교재로 table 수정하기

class DateCheckTest(models.Model): #각 교재별로 조사한 날짜들 저장
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE, to_field='title')
    date = models.DateField(null=True)

class SearchedQuestionListTest(models.Model): #모든 교재에 대해 조사한 질문들 저장
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE, to_field='title')
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    date = models.DateField()
    #img = models.ImageField()

class ExtractedQuestionListTest(models.Model): #추출한 모든 답변 가능 질문들 저장
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE, to_field='title')
    student = models.CharField(max_length=50)
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    #img = models.ImageField()


class FaqAndEstimatedAnswerTest(models.Model): #FAQ와 예상 답변 저장
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE, to_field='title')
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    count = models.IntegerField(default=1)
    keyword1 = models.CharField(max_length=20, null=True)
    keyword2 = models.CharField(max_length=20, null=True)
    keyword3 = models.CharField(max_length=20, null=True)
    answer = models.TextField(default='') 

class AnsweredQuestionListTest(models.Model): #답변 가능 질문 추출 후 실제 답변한 질문들 저장
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE, to_field='title')
    student = models.CharField(max_length=50)
    page = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)   
    answer = models.TextField(null=False)
    #img = models.ImageField()

class BlacklistTest(models.Model): #답변 금지 학생 목록
    student = models.CharField(max_length=50, primary_key=True)