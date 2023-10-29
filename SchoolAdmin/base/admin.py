from django.contrib import admin
from .models import Student, Teacher, Parent, Score, Staff
from .forms import ScoreForm


# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Staff)
