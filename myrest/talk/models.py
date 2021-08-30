from django.contrib.auth.models import User
from django.db import models

from talk.helpers.add_update import Helper


class Post(Helper):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
