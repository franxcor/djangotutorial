from django.urls import path
from . import views
app_name = "polls" # since we only have one app in our workspace

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),

    #these paths automatically run the functsion that are defined in the views file
    
    # /polls/num/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # /polls/num/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # /polls/num/vote
    path("<int:question_id>/vote/", views.vote, name="vote")
]