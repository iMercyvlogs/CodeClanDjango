from django.urls import path
from . import views


app_name='histogramApp'

urlpatterns=[
    path('', views.bokehView, name='histogram_url')
]