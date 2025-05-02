from django.db import models
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

##poll question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    #string method to see the values & not just id
    def __str__(self) :
        return self.question_text
    
    #method to check if published within one day 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

##poll options
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

    #string method to see the values & not just id
    def __str__(self) :
        return self.choice_text