from django.db import models

# Create your models here.

class Users(models.Model):
    _id = models.Field(primary_key=True)
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=300)
    profile = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

