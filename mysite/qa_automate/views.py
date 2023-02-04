from django.shortcuts import render, get_object_or_404
from .models import QuestionEx

# Create your views here.

def index(request):
    question_list = QuestionEx.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'qa_automate/questionex_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(QuestionEx, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/questionex_detail.html', context)

def init(request):
    return render(request, 'qa_automate/init.html')


def calender(request):
    return render(request, 'qa_automate/datepicker.html')