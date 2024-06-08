# from django.test import TestCase
# from .models import QuestionClass
# # Create your tests here.

# class QuestionClassTestCase(TestCase): #create a class that oultines how the testing process will be done
#     def setUp(self):
#         QuestionClass.objects.create(name="python related question",slug="python-question",body="how can python codes be tested iteratively?")
#     #this function uses the already created class(QuestionClass) to create new objects to see if the classes function properly
    

#     def test_qtns_db(self):
#         qtn1=QuestionClass.objects.get(name="python related question")
#         self.assertEqual(qtn1.body())

    #this function tests that the created object can accurately be queried from the database


from django.test import TestCase, Client
from django.urls import reverse

class QuestionListUrlTestCase(TestCase):
    def test_question_list_url(self):
        # Create a test client
        client = Client()

        # Define a test slug
        my_slug = 'test-slug'

        # Reverse the URL for the question list
        url = reverse('question_list_url', kwargs={'my_slug': my_slug})

        # Make a GET request to the URL
        response = client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the view function is called with the correct arguments
        self.assertEqual(response.context['my_slug'], my_slug)

        # Check that the correct template is rendered
        self.assertTemplateUsed(response, 'questionsApp/question_list.html')

        