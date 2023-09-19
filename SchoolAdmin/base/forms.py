from django import forms
from .models import Grade_7_8

class ClassForm(forms.ModelForm):
    class Meta:
        model = Grade_7_8
        fields = ['physics', 'chemistry', 'biology']