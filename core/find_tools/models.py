from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings

User = settings.AUTH_USER_MODEL


class JointModel(models.Model):
    location = models.CharField(max_length=80)
    associate_phrase = models.CharField(max_length=254)


class SearchCaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    nick_name = models.CharField(max_length=70)
    description = models.TextField()
    human_name = models.CharField(max_length=24)
    joint = models.OneToOneField(JointModel, on_delete=models.CASCADE)
































