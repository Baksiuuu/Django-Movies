from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db import models


class Profile(models.Model):
    user = OneToOneField(User, on_delete = models.CASCADE)
    age = models.IntegerField(
        null=True,
        blank=True
    )