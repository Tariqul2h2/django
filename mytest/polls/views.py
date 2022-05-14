from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Questions, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5] 
    #[:5] is a number of question I want to show
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request,'polls/index.html',context)
  

def detail(request,question_id):
    # context = {'question':question}
    try:
        question = Questions.objects.get(pk = question_id)

    except Questions.DoesNotExist:
        raise Http404('Question not exist')
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    # return HttpResponse(f"You are looking at the result of Question {question_id}")
    question = get_object_or_404(Questions, pk = question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    # return HttpResponse(f"you are voting on Question {question_id}")
    from django.http import HttpResponse, HttpResponseRedirect

# ...
def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question':question,'error_message':'Select a correct choice'})
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.

