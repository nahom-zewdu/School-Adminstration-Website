from django.contrib import admin
from django.forms.models import inlineformset_factory
from .models import Student, Teacher, Parent, Subject, Staff
from .forms import SubjectForm


class SubjectInline(admin.StackedInline):
    model = Subject
    form = SubjectForm

class StudentAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Staff)
