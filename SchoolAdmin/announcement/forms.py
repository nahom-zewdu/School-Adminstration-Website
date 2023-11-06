from django import forms
from .models import *


class AnnouncementCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': visible.field.label,
            })

    class Meta:
        model = Announcement
        fields = ['title', 'body']