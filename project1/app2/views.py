from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Postserializer
from . models import Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class PostView(viewsets.ViewSet):

    serializer_class=Postserializer
    queryset=Post.objects.all()
    authentication_classes=[JWTAuthentication] # all authentication can use in that classes
    permission_classes=[IsAuthenticated] #
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


    def create(self,request):
        serializer=Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        orders = Post.objects.all()
        serializer = Postserializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


