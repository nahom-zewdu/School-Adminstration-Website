from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    GRADE_CHOICES = [
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),]

    user = models.OneToOneField(User, on_delete=models.CASCADE) # One to one relationship with user model
    student_id = models.CharField(max_length=6, unique=True, editable=False)
    age = models.CharField(max_length=2)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)