from django import forms
from qa_automate.models import BookListTest


class BookListTestForm(forms.ModelForm):
    class Meta:
        model = BookListTest  # 사용할 모델
        fields = ['title']  # QuestionForm에서 사용할 BookListTest 모델의 속성