from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    author  = models.ForeignKey(User, on_delete = 'CASCADE')
    question_text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank=True, null = True)

    def __str__(self):
        return self.question_text
