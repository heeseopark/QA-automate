from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("자동 답변 사이트입니다.")

def page_question_check(request, book_id, page_number, question_number):
    book = get_object_or_404(Book, id=book_id)
    try:
        pq_check = PageQuestionCheck.objects.get(book=book, page_number=page_number, question_number=question_number)
        pq_check.count += 1
        pq_check.save()
    except PageQuestionCheck.DoesNotExist:
        PageQuestionCheck.objects.create(book=book, page_number=page_number, question_number=question_number)
