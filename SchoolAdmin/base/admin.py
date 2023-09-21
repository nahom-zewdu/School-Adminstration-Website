from django.contrib import admin
from django.forms.models import inlineformset_factory
from .models import Student, Teacher, Parent, Grade
from .forms import GradeForm


class GradeInline(admin.StackedInline):
    model = Grade
    form = GradeForm

class StudentAdmin(admin.ModelAdmin):
    inlines = [GradeInline]

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Parent)
