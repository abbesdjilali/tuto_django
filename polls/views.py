from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from .models import Question,Choice

def index(request):
    latest_question_list = Question.objects.order_by('-date_published')[:5]
    context = {
        'latest_question_list': latest_question_list,
        }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html", {'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    #request.POST['choice'] lèvera une exception KeyError si choice n’est pas spécifié dans les données POST
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{
            'question':question,
            'error_message':"Vous n'avez pas fait de choix"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
