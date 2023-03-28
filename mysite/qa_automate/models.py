from django.db import models

# Create your models here.

class BookListTest(models.Model): #새 교재 나올 때 마다 추가
    title = models.CharField(max_length=200, primary_key=True)

class DateCheckTest(models.Model): #각 교재별로 조사한 날짜들 저장
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE)
    date = models.DateField()

class SearchedQuestionListTest(models.Model): #모든 교재에 대해 조사한 질문들 저장
    question_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE)
    page = models.IntegerField()
    number = models.IntegerField()
    theme = models.IntegerField()
    #img = models.ImageField()

class ExtractedQuestionListTest(models.Model): #추출한 모든 답변 가능 질문들 저장
    question_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE)
    student_name_and_id = models.CharField(max_length=200)
    page = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    theme = models.IntegerField(null=True)
    #img = models.ImageField()

class AnsweredQuestionListTest(models.Model): #답변 가능 질문 추출 후 실제 답변한 질문들 저장
    question_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE)
    student_name_and_id = models.CharField(max_length=200)
    page = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    theme = models.IntegerField(null=True)   
    answer = models.CharField(max_length=400, null=True) 
    #img = models.ImageField()

class FaqAndEstimatedAnswerTest(models.Model): #FAQ와 예상 답변 저장
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE)
    page = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    theme = models.IntegerField(null=True)
    count = models.IntegerField(default=1)
    keyword = models.CharField(max_length=200)
    answer = models.CharField(max_length=400, null=True) 

class BlacklistTest(models.Model): #답변 금지 학생 목록
    student_name_and_id = models.CharField(max_length=200)
