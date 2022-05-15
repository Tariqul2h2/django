from django.http import HttpResponseRedirect
from .models import Questions, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # return Questions.objects.order_by('-pub_date')[:5]
        #[:5] is a number of question I want to show
class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Questions.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'

    # def vote(request, question_id):
    #     question = get_object_or_404(Questions, pk=question_id)
    #     try:
    #         selected_choice = question.choice_set.get(pk = request.POST['choice'])
    #     except (KeyError, Choice.DoesNotExist):
    #         return render(request, 'polls/detail.html',{'question':question,'error_message':'Select a correct choice'})
    #     else:
    #         selected_choice.vote += 1
    #         selected_choice.save()
    #         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    #     #     # Always return an HttpResponseRedirect after successfully dealing
    #     #     # with POST data. This prevents data from being posted twice if a
    #     #     # user hits the Back button.

def vote(request, question_id):
    questions = get_object_or_404(Questions, pk=question_id)
    print(questions)
    try:
        selected_choice = questions.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'questions': questions,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(questions.id,)))