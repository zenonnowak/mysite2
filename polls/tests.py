"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from datetime import datetime

from django.test import TestCase

from polls.models import Poll

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
class PollsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)



class PollTest(TestCase):

    def setUp(self):
        question="What is your favourite colour?"
        now = datetime.now()
        self.poll = Poll.objects.create(question=question, pub_date=now)
        self.poll.choice_set.create(choice="Red", votes=0)
        self.poll.choice_set.create(choice="Bue", votes=0)
        self.poll.choice_set.create(choice="Green", votes=0)

    def test_models(self):
        self.assertEqual(self.poll.choice_set.all().count(), 3)