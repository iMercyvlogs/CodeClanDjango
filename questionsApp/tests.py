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