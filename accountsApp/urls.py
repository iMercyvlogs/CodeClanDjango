from django.urls import path
from .import views


app_name='accountsApp'

urlpatterns=[
    path('signup/',views.signup_view,name="signup_view_url"),
    path('login/',views.login_view,name="login_view_url"),
    path('logout/',views.logout_view,name="logout_view_url"),
]