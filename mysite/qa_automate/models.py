from django.db import models
from datetime import date

# Create your models here.

class BookTest(models.Model):
    title = models.CharField(max_length=200, primary_key=True)

class DateCheckTest(models.Model):
    book = models.ForeignKey(BookTest, on_delete=models.CASCADE)
    date = models.DateField()

class QuestionListTest(models.Model):
    question_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookTest, on_delete=models.CASCADE)
    question_number = models.IntegerField()
    student_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=20)
    page = models.IntegerField()
    number = models.IntegerField()
    theme = models.IntegerField()
    example = models.IntegerField()

class BlacklistTest(models.Model):
    student_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=20)

    