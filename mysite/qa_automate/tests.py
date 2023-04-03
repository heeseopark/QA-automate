from .models import SearchedQuestionListTest


# Create your tests here.

question = SearchedQuestionListTest(question_id = 1234, book = '수학의 시작, 시발점 - 수학l', student_name_and_id = 123, page = 12, number = 34, theme = 56, answer = None)
question.save()