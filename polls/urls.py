from django.urls import path
from . import views
app_name = "polls" # since we only have one app in our workspace

urlpatterns = [
    path("", views.index, name="index"),

    #these paths automatically run the functsion that are defined in the views file
    
    # /polls/num/
    path("<int:question_id>/", views.detail, name="detail"),

    # /polls/num/results
    path("<int:question_id>/results", views.results, name="results"),

    # /polls/num/vote
    path("<int:question_id>/vote/", views.vote, name="vote")
]