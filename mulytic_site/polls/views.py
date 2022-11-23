from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Questions
from django.template import loader

# Create your views here.

def index(request):
    # return HttpResponse('Hello you are in Poll app')
    latest_question_list = Questions.objects.order_by('-pub_time')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    # return HttpResponse(f'You are looking at question number {question_id}')
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist as e:
        raise Http404(f'Question {question_id} does not exist')
    return render(request,'polls/detail.html',{'question':question})


def results(request, question_id):
    return HttpResponse(f'You are looking at the results of question number {question_id}')

def vote(request,question_id):
    return HttpResponse(f'You are voting on question number {question_id}')