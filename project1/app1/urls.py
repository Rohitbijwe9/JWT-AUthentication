from django.urls import path
from .views import UserAPI
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh



urlpatterns=[
    path('user/',UserAPI.as_view()),         #create user
    path('access/',token_obtain_pair),       #get access and refresh token    
    path('refresh/',token_refresh)           #by using refresh get access after 5 min
]
