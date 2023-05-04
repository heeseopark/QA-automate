from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models_v1 import BookList, BlackList, DateCheck, FaqAndEstimatedAnswer, SearchedQuestionList, ExtractedAndAnsweredQuestionList
from .functions import goToWaitingPage, updateSearchedAndFaqTable, goToTotalPage, extractquestions
from datetime import datetime, timedelta

# Create your views here.

def init(request):
    return render(request, 'qa_automate/init.html')

def booklist(request):
    books = BookList.objects.all().order_by('title')

    if request.method == 'POST':
        title = request.POST.get('title').strip()
        lecture = request.POST.get('lecture').strip()
        booktype = request.POST.get('book_type').strip()
        book = BookList(title=title, lecture=lecture, type = booktype)
        book.save()
        return HttpResponseRedirect('/qa_automate/booklist/')
    
    context = {
        'books': books,
    }
    
    return render(request, 'qa_automate/booklist.html', context)



def calendar(request, book_title):
    book = BookList.objects.get(title=book_title)
    date_checks = DateCheck.objects.filter(book=book).order_by('date')

    if request.method == 'POST':
        startdate_str = request.POST.get('startdate')
        enddate_str = request.POST.get('enddate')
        startdate = datetime.strptime(startdate_str, '%Y-%m-%d')
        enddate = datetime.strptime(enddate_str, '%Y-%m-%d')

        # DateCheck DB 업데이트
        current_date = startdate
        while current_date <= enddate:
            if not DateCheck.objects.filter(book=book, date=current_date).exists():
                date_check = DateCheck(book=book, date=current_date)
                date_check.save()
            current_date += timedelta(days=1)

        # Searched DB, FaQ DB 업데이트
        lecture_str = str(BookList.objects.get(title = book_title).lecture).strip()
        updateSearchedAndFaqTable(startdate_str, enddate_str, lecture_str)

    lecture_str = str(BookList.objects.get(title = book_title).lecture).strip()
    context = {
        'lecture': lecture_str,
        'searched_dates': date_checks,
        'book' : book
    }
    return render(request, 'qa_automate/calendar.html', context)

def searched(request, book_title):
    book_text = str(book_title).strip()
    questions = SearchedQuestionList.objects.filter(book__title=book_text).order_by('id')
    print(book_title)
    print(book_text)

    if request.method == 'GET':
        page_num = request.GET.get('page_num')
        theme_num = request.GET.get('theme_num')
        question_num = request.GET.get('question_num')
        if page_num:
            questions = questions.filter(page=page_num)
        if theme_num:
            questions = questions.filter(theme=theme_num)
        if question_num:
            questions = questions.filter(number=question_num)
    return render(request, 'qa_automate/searchedlist.html', {'questions': questions, 'book': book_text})


def blacklist(request):
    elements = BlackList.objects.all()
    if request.method == 'POST':
        student_name_and_id = request.POST.get('student_name_and_id').strip()
        element = BlackList(student=student_name_and_id)
        element.save()
        return HttpResponseRedirect('/qa_automate/blacklist/')
    return render(request, 'qa_automate/blacklist.html', {'elements': elements})


def faqlist(request):
    books = FaqAndEstimatedAnswer.objects.values_list('book__title', flat=True).distinct()
    if request.method == 'GET':
        selected_book = request.GET.get('book')
        if selected_book == '':
            unanswerable_questions = FaqAndEstimatedAnswer.objects.filter(answer='', count__gt=10).exclude(page=0).order_by('-count')
            answerable_questions = FaqAndEstimatedAnswer.objects.exclude(answer='', count__gt=10).order_by('-count')
        else:
            unanswerable_questions = FaqAndEstimatedAnswer.objects.filter(answer='', book=selected_book, count__gt=10).exclude(page=0).order_by('-count')
            answerable_questions = FaqAndEstimatedAnswer.objects.filter(book=selected_book, count__gt=10).exclude(answer='').order_by('-count')
    else:
        unanswerable_questions = FaqAndEstimatedAnswer.objects.filter(answer='', count__gt=10).exclude(page=0).order_by('-count')
        answerable_questions = FaqAndEstimatedAnswer.objects.exclude(answer='', count__gt=10).order_by('-count')

    context = {
        'unanswerable_questions': unanswerable_questions,
        'answerable_questions': answerable_questions,
        'books': books,
    }
    return render(request, 'qa_automate/faqlist.html', context)



def estimatedanswer(request, book_title, page, theme, number):
    # Get the matching question object
    question = FaqAndEstimatedAnswer.objects.get(
        book=book_title, page=page, theme=theme, number=number)

    # Check if there's already an estimated answer for the question
    try:
        faq = FaqAndEstimatedAnswer.objects.get(
            book=book_title, page=page, theme=theme, number=number)
        answer = faq.answer
    except FaqAndEstimatedAnswer.DoesNotExist:
        answer = ''

    if request.method == 'POST':
        answer = request.POST['answer']
        # 키워드 받아서 저장하기
        # Check if there's already an estimated answer for the question
        try:
            faq = FaqAndEstimatedAnswer.objects.get(
                book=book_title, page=page, theme=theme, number=number)
            faq.answer = answer
            faq.save()
        except FaqAndEstimatedAnswer.DoesNotExist:
            book = BookList.objects.get(title=book_title)
            faq = FaqAndEstimatedAnswer(
                book=book, page=page, theme=theme, number=number, answer=answer)
            faq.save()

    return render(request, 'qa_automate/estimatedanswer.html', {'question': question, 'answer': answer})


def test(request):
    return render(request, 'qa_automate/booklist.html')

def extract(request):
    if request.method == 'POST' and 'answerquestions' in request.POST:
        # Handle the case when the form with name `answerquestions` is submitted
        pass
        # html에 남아있는 것들 answered question list로 옮기고, 답변 이미 되어서 질문이 없거나, 다른 사람이 답변 중인 경우 그냥 빈 return 던지기
        # waiting page에서 id로 1개씩 찾아서 해야할듯 (매번 for loop 돌리는 것보다 빠름)
        # 지금 false로 되어 있는 것들 다 true로 바꾸기
        
    if request.method == 'POST' and 'extractquestions' in request.POST:
        # Handle the case when the form with name `extractquestions` is submitted
        extractquestions()
    

    if request.method == 'POST' and 'deletequestion' in request.POST:
        print(request)
        id = int(request.POST.get('question_id'))
        question = ExtractedAndAnsweredQuestionList.objects.get(id = id)
        question.delete()

    extracted_questions = ExtractedAndAnsweredQuestionList.objects.filter(done=False).order_by('priority')

    ### context 만들기 (python 단에서 queryset들을 만들고 한번에 html에서 render 해야함)
    context = {
        'questions': extracted_questions,
    }

    return render(request, 'qa_automate/extract.html', context)


