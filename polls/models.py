from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

##poll question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    #string method to see the values & not just id
    def __str__(self) :
        return self.question_text
    
    
    @admin.display(
        boolean=True,
        description="Choices?"
    )
    def has_choices(self):
        return self.choice_set.exists()
    
    # changing the displayh of the admin
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?"
    )
    #method to check if published within one day 
    def was_published_recently(self):  #needs to be below the admin display
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



##poll options
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

    #string method to see the values & not just id
    def __str__(self) :
        return self.choice_text