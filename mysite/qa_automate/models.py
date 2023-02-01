from django.db import models
from datetime import date

# Create your models here.

from django.db import models

class DateCheck(models.Model):
    date = models.DateField()
    is_checked = models.BooleanField(default=False)

class PageQuestionCheck(models.Model):
    page_number = models.PositiveIntegerField()
    question_number = models.PositiveIntegerField()
    count = models.PositiveIntegerField(default=1)

