from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect, HttpResponsePermanentRedirect
from django.urls import reverse
from .models import Student, Teacher

# Create your views here.

def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
        'students': students,
    }
    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)

    return HttpResponsePermanentRedirect(reverse('base:home'))


def student_login(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        password = request.POST['password']

        user = authenticate(request, student_id=student_id, password=password)
        if user:
            login(request, user)
            return redirect('base:home')
        else:
            error_message = 'Invalid ID number or Password'
            return render(request, 'student_login.html', {'error_message': error_message})
    else:
        return render(request, 'student_login.html')



def teacher_login(request):
    if request.method == 'POST':
        teacher_id = request.POST['teacher_id']
        password = request.POST['password']

        user = authenticate(request, teacher_id=teacher_id, password=password)
        if user:
            login(request, user)
            return redirect('base:home')
        else:
            error_message = 'Invalid ID number or Password'
            return render(request, 'teacher_login.html', {'error_message': error_message})
    else:
        return render(request, 'teacher_login.html')


def parent_login(request):
    if request.method == 'POST':
        parent_id = request.POST['parent_id']
        password = request.POST['password']

        user = authenticate(request, parent_id=parent_id, password=password)
        if user:
            login(request, user)
            return redirect('base:home')
        else:
            error_message = 'Invalid ID number or Password'
            return render(request, 'parent_login.html', {'error_message': error_message})
    else:
        return render(request, 'parent_login.html')