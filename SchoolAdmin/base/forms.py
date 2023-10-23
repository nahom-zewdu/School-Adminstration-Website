from django import forms
from django.contrib.auth.models import User
from .models import *


class StudentCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'gender', 'grade', 'parent_phone']

class TeacherCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

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
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'email', 'parent_to', 'phone']
        

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'