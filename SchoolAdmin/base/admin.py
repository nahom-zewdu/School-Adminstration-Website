from django.contrib import admin
from django.forms.models import inlineformset_factory
from .models import Student, Teacher, Parent, Grade_7_8
from .forms import Grade_7_8_Form


class Grade_7_8_Inline(admin.StackedInline):
    model = Grade_7_8
    form = Grade_7_8_Form

class StudentAdmin(admin.ModelAdmin):
    inlines = [Grade_7_8_Inline]

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Parent)
