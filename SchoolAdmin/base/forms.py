from django import forms
from django.contrib.auth.models import User
from .models import Subject, Student


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
        fields = ['first_name', 'last_name','email', 'age', 'gender', 'grade', 'parent_phone']



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'