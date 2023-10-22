from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, HttpResponsePermanentRedirect
from django.urls import reverse
from .models import Student, Teacher, Subject

# Create your views here.

def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
        'students': students,
    }
    return render(request, 'base/home.html', context)


def dashboard(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    
    female_students = Student.filter_by_gender('F')
    male_students = Student.filter_by_gender('M')

    female_teachers = Teacher.filter_by_gender('F')
    male_teachers = Teacher.filter_by_gender('M')
    
    context = {
        'teachers': teachers,
        'students': students,
        'female_students': female_students,
        'male_students': male_students,
        'female_teachers': female_teachers,
        'male_teachers': male_teachers,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='/restricted/')
def student_academics(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    female = Student.filter_by_gender('F')
    male = Student.filter_by_gender('M')
    context = {
        'students': students,
        'subjects': subjects,
        'female': female,
        'male': male,
    }

    return render(request, 'student_academics.html', context)


@login_required(login_url='/restricted/')
def teacher_academics(request):
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    female = Teacher.filter_by_gender('F')
    male = Teacher.filter_by_gender('M')
    context = {
        'teachers': teachers,
        'subjects': subjects,
        'female': female,
        'male': male,
    }
    return render(request, 'teacher_academics.html', context)


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
            return render(request, 'login/student_login.html', {'error_message': error_message})
    else:
        return render(request, 'login/student_login.html')



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
            return render(request, 'login/teacher_login.html', {'error_message': error_message})
    else:
        return render(request, 'login/teacher_login.html')


def staff_login(request):
    if request.method == 'POST':
        staff_id = request.POST['staff_id']
        password = request.POST['password']

        user = authenticate(request, staff_id=staff_id, password=password)
        if user:
            login(request, user)
            return redirect('base:home')
        else:
            error_message = 'Invalid ID number or Password'
            return render(request, 'login/staff_login.html', {'error_message': error_message})
    else:
        return render(request, 'login/staff_login.html')

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
            return render(request, 'login/parent_login.html', {'error_message': error_message})
    else:
        return render(request, 'login/parent_login.html')

def restricted_view(request):
    return render(request, 'base/restricted.html')