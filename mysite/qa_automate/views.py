from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models_v1 import BookList, BlackList, DateCheck, FaqAndEstimatedAnswer, SearchedQuestionList, ExtractedAndAnsweredQuestionList
from .functions import updateSearchedAndFaqTable, extractquestions, answer, getqas
from datetime import datetime, timedelta
from django.db.models import Min

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

def qa(request):
    # Get distinct book titles from the BookList
    books = BookList.objects.values_list('title', flat=True).distinct()

    qas=[]

    # Initialize ids to an empty queryset
    ids = SearchedQuestionList.objects.none()

    if request.method == 'GET' and 'extractquestions' in request.GET:
        selected_book = request.GET.get('book')
        page_num = request.GET.get('page_num')
        theme_num = request.GET.get('theme_num')
        question_num = request.GET.get('question_num')

        # If book is selected, filter by book title
        if selected_book:
            ids = SearchedQuestionList.objects.filter(book__title=selected_book).order_by('id')
        
        # Further filter the queryset based on provided page, theme, and question number
        if page_num:
            ids = ids.filter(page=page_num)
        if theme_num:
            ids = ids.filter(theme=theme_num)
        if question_num:
            ids = ids.filter(number=question_num)
        
        # Get id list
        ids = ids.values_list('id', flat=True)

        # Extract the earliest date from the filtered queryset
        start_date = ids.aggregate(Min('date'))['date__min']

        qas = getqas(str(start_date), ids)


    context = {
        'qas' : qas,
        'books': books,
    }
    return render(request, 'qa_automate/qa.html', context)




def faqlist(request):
    books = FaqAndEstimatedAnswer.objects.values_list('book__title', flat=True).distinct()
    if request.method == 'GET':
        selected_book = request.GET.get('book')
        if selected_book == '':
            unanswerable_questions = FaqAndEstimatedAnswer.objects.filter(answer='', count__gt=10).exclude(page=0).order_by('-count')
            answerable_questions = FaqAndEstimatedAnswer.objects.exclude(answer='', count__gt=10).order_by('-page')
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
        keywords = faq.keywords
    except FaqAndEstimatedAnswer.DoesNotExist:
        answer = ''

    if request.method == 'POST':
        answer = request.POST['answer']
        keywords = request.POST['keywords']
        # 키워드 받아서 저장하기
        # Check if there's already an estimated answer for the question
        try:
            faq = FaqAndEstimatedAnswer.objects.get(
                book=book_title, page=page, theme=theme, number=number)
            faq.answer = answer
            faq.keywords = keywords
            faq.save()
        except FaqAndEstimatedAnswer.DoesNotExist:
            book = BookList.objects.get(title=book_title)
            faq = FaqAndEstimatedAnswer(
                book=book, page=page, theme=theme, number=number, answer=answer, keywords = keywords)
            faq.save()

    return render(request, 'qa_automate/estimatedanswer.html', {'question': question, 'answer': answer, 'keywords': keywords})


def test(request):
    return render(request, 'qa_automate/booklist.html')

def extract(request):
    if request.method == 'POST' and 'answerquestions' in request.POST:
        # Handle the case when the form with name `answerquestions` is submitted
        answer()
        return HttpResponseRedirect('/qa_automate/extract/')
        # html에 남아있는 것들 answered question list로 옮기고, 답변 이미 되어서 질문이 없거나, 다른 사람이 답변 중인 경우 그냥 빈 return 던지기

        
    if request.method == 'POST' and 'extractquestions' in request.POST:
        # Handle the case when the form with name `extractquestions` is submitted

        questions_with_empty_answers = ExtractedAndAnsweredQuestionList.objects.filter(done = False)
        questions_with_empty_answers.delete()
        extractquestions()
        
        return HttpResponseRedirect('/qa_automate/extract/')
    

    if request.method == 'POST' and 'deletequestion' in request.POST:
        id = int(request.POST.get('question_id'))
        question = ExtractedAndAnsweredQuestionList.objects.get(id = id)
        question.delete()
        return HttpResponseRedirect('/qa_automate/extract/')

    # Handle the case when the form with name `saveallanswers` is submitted
    if request.method == 'POST' and 'saveallanswers' in request.POST:
        question_ids = request.POST.getlist('question_ids')
        for id in question_ids:
            id = int(id)
            edited_answer = request.POST.get(f'edited_answer_{id}')
            question = ExtractedAndAnsweredQuestionList.objects.get(id=id)
            question.answer = edited_answer
            question.save()
            print(f'question id {id} is saved')
        return HttpResponseRedirect('/qa_automate/extract/')

    extracted_questions = ExtractedAndAnsweredQuestionList.objects.filter(done=False).order_by('-priority')

    ### context 만들기 (python 단에서 queryset들을 만들고 한번에 html에서 render 해야함)
    context = {
        'questions': extracted_questions,
    }

    return render(request, 'qa_automate/extract.html', context)


