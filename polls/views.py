from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Question

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
    return HttpResponse("Page résultats pour la question : %s" %question_id)

def vote(request,question_id):
    return HttpResponse("Votez pour la question %s" %question_id)