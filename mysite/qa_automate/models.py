from django.db import models

# Create your models here.

class BookListTest(models.Model):
    title = models.CharField(max_length=200, primary_key=True)

class DateCheckTest(models.Model):
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE)
    date = models.DateField()

class QuestionListTest(models.Model):
    question_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookListTest, on_delete=models.CASCADE)
    student_name_and_id = models.CharField(max_length=200)
    page = models.IntegerField()
    number = models.IntegerField()
    theme = models.IntegerField()
    #  img = models.ImageField
    class Meta:
        abstract = True

class FaqListTest(QuestionListTest):
    count = models.IntegerField(default=1)
    keyword = models.CharField(max_length=200)    

class EstimatedAnswerTest(QuestionListTest):
    answer = models.CharField(max_length=400)

class BlacklistTest(models.Model):
    student_name_and_id = models.CharField(max_length=200)

    