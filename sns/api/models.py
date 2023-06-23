from django.db import models

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    # user_posts = models.ManyToManyField("Post", null=True) # posts created by this user

class Post(models.Model):
    dislikes = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_posts",)
