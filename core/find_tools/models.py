from django.db import models
from ..useraccount.models import User
from django.contrib.auth.models import AbstractUser
import uuid


class JointModel(models.Model):
    location = models.CharField(max_length=80)
    associate_phrase = models.CharField(max_length=254)



class SearchCaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    description = models.TextField()
    human_name = models.CharField


















