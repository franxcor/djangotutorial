from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice


# this class tests with date time
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self) :
        #this is what we are testing
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        #this is what the result of the test should be 
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self) :
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

#shortcut function to create a new question
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date= time)

def create_choice(question, choice_text, votes):
    return Choice.objects.create(question=question, choice_text=choice_text, votes=votes)

# this class tests the front end messages & response are correct
class QuestionIndexViewTests(TestCase):

    #in the case that there are no questions
    def test_no_question(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")

    #the past question should be displayed 
    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    #the future question should not be displayed
    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])
    
    #only the past question should be displayed
    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    #both past questions should be displayed
    def test_two_past_question(self):
        question1 = create_question(question_text="Past question 1", days=-30)
        question2 = create_question(question_text="Past question 2", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )

#validity of detail pages
class QuestionDetailViewTests(TestCase):
    # detail view of a future question should return a 404 message
    def test_future_question_details(self):
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # detail view should display questions text
    def test_past_question_details(self):
        question = create_question(question_text="Past Question", days=-30)
        url = reverse("polls:detail", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class QuestionResultsViewTests(TestCase):
    #results view of a future question should return a 404 message
    def test_future_question_results(self):
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:results", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question_results(self):
        question = create_question(question_text="Past Question", days=-30)
        url = reverse("polls:results", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ExtraTests(TestCase):
    def setUp(self):
        pq1 = create_question(question_text="Past Question 1.", days=-5)
        create_choice(pq1, choice_text="Choice 1", votes=0)
        create_choice(pq1, choice_text="Choice 2", votes=0)
        create_choice(pq1, choice_text="Choice 3", votes=0)

        create_question(question_text="Past Question 2. ", days=-2)
        
        create_question(question_text="Future Question 1. ", days=2)
        create_question(question_text="Future Question 2. ", days=5)
    
    def test_has_choices(self):
        pq1 = Question.objects.get(question_text="Past Question 1.")
        pq2 = Question.objects.get(question_text="Past Question 2. ")
        self.assertTrue(pq1.has_choices())
        self.assertFalse(pq2.has_choices())
