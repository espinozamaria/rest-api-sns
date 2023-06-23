# from django.contrib.auth.models import User
from rest_framework import serializers
from sns.api.models import Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email', 
            'name', 
            'user_posts',
            'password',
            'token',
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 
            'user',
            'likes', 
            'dislikes',
            'views'
        )

