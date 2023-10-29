from django import forms
from django.contrib.auth.models import User
from .models import *


class StudentCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': visible.field.label,
            })

    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email','image', 'age', 'gender', 'grade', 'parent_phone']

class TeacherCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': visible.field.label,
            })

    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'gender', 'department', 'experience', 'phone']


class ParentCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': visible.field.label,
            })

    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'email', 'phone']


class StaffCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': visible.field.label,
            })

    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone']


class ExcelImportForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': visible.field.label,
            })
    file = forms.FileField(required=True)

class StudentCreationFormWithFile(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'gender', 'grade', 'parent_phone']

class TeacherCreationFormWithFile(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'gender']

class ScoreForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': visible.field.label,
            })
    SEMESTER_CHOICE =[
        ('First Semester', '1st'),
        ('Second Semester', '2nd')
    ]
    GRADE_CHOICES = [
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
    ]

    grade = forms.ChoiceField(choices=GRADE_CHOICES, required=True)
    semester = forms.ChoiceField(choices=SEMESTER_CHOICE, required=True)
    file = forms.FileField(required=True)
    

class PublishScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['semester' ,'physics', 'biology', 'chemistry', 'average', 'rank']