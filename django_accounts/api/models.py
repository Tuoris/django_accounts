from django.db import models

class Account(models.Model):
    avatar = models.ImageField(null=True)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    creation_date = models.DateField(auto_now=True)
