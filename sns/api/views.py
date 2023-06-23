from django.shortcuts import render
# from django.contrib.auth.models import User, Post
from rest_framework import viewsets
from rest_framework import permissions, response
from sns.api.serializers import UserSerializer, PostSerializer
from sns.api.models import User, Post
from django.conf import settings
import requests
import json


class UserViewUpdate(viewsets.ModelViewSet):
    """
    View or edit users
    """
    print('user view update')
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CreateUser(viewsets.ModelViewSet):
    """
    Create a new user
    """

    queryset = User.objects.all()
    print('inside create user view')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def validate_email(self, payload):
        url = "https://emailvalidation.abstractapi.com/v1/?api_key=" + settings.EMAIL_VALIDATION_API + "&email=" + payload + "&auto_correct=false"
        response = requests.get(url)
        api_data = json.loads(response.content)
        return api_data['is_valid_format']['value']

    def create(self, request):
        email_validation = self.validate_email(request.data['email'])
        print('email veri', email_validation)
        if email_validation is False:
            return response.Response("Check email formatting")
        return response.Response(request.data)

class LoginUser(viewsets.ModelViewSet):
    """
    Create a new user
    """
    print('user login ')
    # queryset = User.objects.get(user=self.request.user) 
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewUpdate(viewsets.ModelViewSet):
    """
    View or edit posts
    """
    print('post view update')
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CreatePost(viewsets.ModelViewSet):
    """
    Create a new user
    """
    print('user create ')
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

