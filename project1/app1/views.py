from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import User,UserSerializer


class UserAPI(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset=User.objects.all()
    