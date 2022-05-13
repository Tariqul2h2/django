from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Questions

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# def index(request):
#     return HttpResponse('Hello, this a test only')


# def index(request):
#     latest_question_list = Questions.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5] 
    #[:5] is a number of question I want to show
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request,'polls/index.html',context)
  

def detail(request,question_id):
    context = {
        'question':question
    }
    try:
        question = Questions.objects.get(pk = question_id)

    except Questions.DoesNotExist:
        raise Http404('Question not exist')
    return render(request, 'polls/details.html',context)
    # return HttpResponse(f"You are looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You are looking at the result of Question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"you are voting on Question {question_id}")
