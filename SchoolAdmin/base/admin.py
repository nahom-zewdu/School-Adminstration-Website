from django.contrib import admin
from django.forms.models import inlineformset_factory
from .models import Student, Teacher, Parent, Score, Staff
from .forms import ScoreForm


class ScoreInline(admin.StackedInline):
    model = Score
    form = ScoreForm

class StudentAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Staff)
