from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone

def home(request) :
    return render(request, 'home.html')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


#remains same
def vote(request, question_id):
    # check valid question
    question = get_object_or_404(Question, pk=question_id)
    try:
        #since it is a radio, if the choice is not valid, it would be no select
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice." #this fills in the error message we put in earler
            },
        )
    else:
        selected_choice.votes=F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))





'''
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

from django.http import Http404 #original if question id doesn't exist method

from django.db.models import F
from django.urls import reverse
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
    
    try :
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
    

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


        '''