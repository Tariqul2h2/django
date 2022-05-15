from time import time
from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Questions

class QuestionsModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        print(time)
        future_questions = Questions(pub_date = time)
        self.assertIs(future_questions.was_published_recently(),False)


# Create your tests here.
