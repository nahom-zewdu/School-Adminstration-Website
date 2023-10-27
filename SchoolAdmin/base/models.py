from django.db import models
from django.contrib.auth.models import User

import random
# Create your models here.



class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    GRADE_CHOICES = [
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Student')
    name = models.CharField(max_length=44, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='profile/', default='user.jpg')
    student_id = models.CharField(max_length=6, unique=True, editable=False)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=False, blank=False)
    parent_phone = models.CharField(max_length=20, null=True, blank=True)

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

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
    
    @classmethod
    def filter_by_grade(cls, grade):
        return cls.objects.filter(grade=grade) 

    def __str__(self):
        return self.name



class Teacher(models.Model):
    DEPARTMENT_CHOICES = [
        ('Social Studies', 'Social' ),
        ('Natural Science', 'Natural'),
        ('Physical Education', 'Sport'),
        ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='Teacher')
    name = models.CharField(max_length=44, null=True, blank=True)
    teacher_id = models.CharField(max_length=6, editable=False, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False, null=False)
    department = models.CharField(max_length=20,choices=DEPARTMENT_CHOICES, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True, default=3)
    phone = models.CharField(max_length=20, null=True, blank=True)


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
    phone = models.CharField(max_length=20, blank=False, null=False)


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


class Staff(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=44, null=True, blank=True)
    staff_id = models.CharField(max_length=6, editable=False, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)

    
    @classmethod
    def filter_by_gender(cls, gender):
        return cls.objects.filter(gender=gender) 

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        if not self.staff_id:
            self.staff_id = self.generate_unique_staff_id()
        super().save(*args, **kwargs)

    def generate_unique_staff_id(self):
        while True:
            staff_id = '27' +  str(random.randint(1000, 9999))
            if not Staff.objects.filter(staff_id=staff_id).exists():
                return staff_id

    def __str__(self):
        return self.name
        

class Score(models.Model):
    SEMESTER_CHOICE =[
        ('First Semester', '1st'),
        ('Second Semester', '2nd')
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    semester = models.CharField(max_length=30, choices=SEMESTER_CHOICE, null=False, blank=False)
    physics = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    chemistry = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    biology = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    average = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    rank = models.IntegerField(null=False, blank=False)
    
    
    def __str__(self):
        return str(self.rank)