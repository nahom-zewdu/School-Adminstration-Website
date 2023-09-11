from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One to one relationship with user model
    student_id = models.CharField(max_length=6, unique=True, editable=False)
    age = models.CharField(max_length=2)

    