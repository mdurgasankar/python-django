from django.db import models
from django.contrib import auth
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete='CASCADE',default=1)
    post = models.CharField(max_length=250)
    comment = models.TextField()
    is_active = models.BooleanField(default=True)


class comments(models.Model):
    post = models.ForeignKey(Post, on_delete='CASCADE')
    comment = models.TextField()
