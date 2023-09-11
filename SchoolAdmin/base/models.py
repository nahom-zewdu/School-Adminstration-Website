from django.db import models
from django.contrib.auth.models import User

import random
# Create your models here.

class Student(models.Model):
    GRADE_CHOICES = [
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One to one relationship with user model
    student_id = models.CharField(max_length=6, unique=True, editable=False)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Unknown', null=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.student_id = self.generate_unique_student_id()
        super().save(*args, **kwargs)

    def generate_unique_student_id(self):
        while True:
            student_id = '19' +  str(random.randint(1000, 9999))
            if not Student.objects.filter(student_id=student_id).exists():
                return student_id


class Teacher(models.Model):
    GRADE_CHOICES = [
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    teacher_id = models.CharField(max_length=6, editable=False, unique=True)
    subject = models.CharField(max_length=20, null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Unknown', null=True)
    qualifications = models.CharField(max_length=30)
    experience = models.IntegerField()
    teaches_grade = models.CharField(max_length=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.teacher_id = self.generate_unique_teacher_id()
        super().save(*args, **kwargs)

    def generate_unique_teacher_id(self):
        while True:
            teacher_id = '12' +  str(random.randint(1000, 9999))
            if not Student.objects.filter(teacher_id=teacher_id).exists():
                return teacher_id
