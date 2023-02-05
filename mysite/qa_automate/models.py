from django.db import models
from datetime import date

# Create your models here.

class DateCheck(models.Model):
    date = models.DateField()
    is_checked = models.BooleanField(default=False)

class Question(models.Model):
    page_number = models.PositiveIntegerField(default=1)
    question_number = models.PositiveIntegerField(default=1)
    count = models.PositiveIntegerField(default=1)

class SibalSooSangDate(DateCheck):
    pass

class SibalSooSangQuestion(Question):
    pass

class QuestionEx(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class AnswerEx(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()