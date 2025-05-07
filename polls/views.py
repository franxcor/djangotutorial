from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

from django.http import Http404 #original if question id doesn't exist method

from django.template import loader
# Create your views here.
def index(request) :
    #this displays all the question in a bulleted list when you visit the /polls/ page
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    #output = ", ".join([q.question_text for q in latest_question_list]) -> this was the cs list
    #return HttpResponse(template.render(context, request)) -> the original without shortcut
    return render(request, "polls/index.html", context) #uses the render function shortcut

    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #what we are doing in the try
    return render(request, "polls/detail.html", {"question" : question})

    # add a try/except in case a question doesn't exist. 
    '''
    try :
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
    '''

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)