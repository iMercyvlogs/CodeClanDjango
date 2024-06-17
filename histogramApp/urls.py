from django.urls import path
from . import views


app_name='histogramApp'

urlpatterns=[
    path('', views.histogramDisplay, name='histogram_url')
]