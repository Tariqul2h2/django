from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Questions, Choice
from django.template import loader
from django.urls import reverse


# Create your views here.

def index(request):
    # return HttpResponse('Hello you are in Poll app')
    latest_question_list = Questions.objects.order_by('-pub_time')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # return HttpResponse(f'You are looking at question number {question_id}')
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist as e:
        raise Http404(f'Question {question_id} does not exist')
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # return HttpResponse(f'You are looking at the results of question number {question_id}')


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError(Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You did not select any choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse(f'You are voting on question number {question_id}')
