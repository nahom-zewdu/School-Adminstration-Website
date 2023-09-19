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
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Student') # One to one relationship with user model
    name = models.CharField(max_length=44, null=True, blank=True)
    student_id = models.CharField(max_length=6, unique=True, editable=False)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Unknown', null=True)
    # grade = models.CharField(max_length=2, choices=GRADE_CHOICES, null=False, blank=False)
    # grade_7_8 = models.ForeignKey(Grade_7_8, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        if not self.student_id:
            self.student_id = self.generate_unique_student_id()
        super().save(*args, **kwargs)

    def generate_unique_student_id(self):
        while True:
            student_id = '19' +  str(random.randint(1000, 9999))
            if not Student.objects.filter(student_id=student_id).exists():
                return student_id

    @classmethod
    def filter_by_gender(cls, gender):
        return cls.objects.filter(gender=gender) 

    def __str__(self):
        return self.name



class Grade_7_8(models.Model):
    physics = models.CharField(max_length=4)
    chemistry = models.CharField(max_length=4)
    biology = models.CharField(max_length=4)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name
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

    user = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='Teacher')
    name = models.CharField(max_length=44, null=True, blank=True)
    teacher_id = models.CharField(max_length=6, editable=False, unique=True)
    subject = models.CharField(max_length=20, null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Unknown', null=True)
    qualifications = models.CharField(max_length=30)
    experience = models.IntegerField()
    teaches_grade = models.CharField(max_length=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        if not self.teacher_id:
            self.teacher_id = self.generate_unique_teacher_id()
        super().save(*args, **kwargs)

    def generate_unique_teacher_id(self):
        while True:
            teacher_id = '12' +  str(random.randint(1000, 9999))
            if not Teacher.objects.filter(teacher_id=teacher_id).exists():
                return teacher_id


    @classmethod
    def filter_by_gender(cls, gender):
        return cls.objects.filter(gender=gender) 
        
    def __str__(self):
        return self.name

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Parent')
    name = models.CharField(max_length=44, null=True, blank=True)
    parent_id = models.CharField(max_length=6, editable=False, unique=True)
    parent_to = models.ManyToManyField(Student)
    phone_no = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        if not self.parent_id:
            self.parent_id = self.generate_unique_parent_id()
        super().save(*args, **kwargs)

    def generate_unique_parent_id(self):
        while True:
            parent_id = '21' +  str(random.randint(1000, 9999))
            if not Parent.objects.filter(parent_id=parent_id).exists():
                return parent_id

    def __str__(self):
        return self.name


