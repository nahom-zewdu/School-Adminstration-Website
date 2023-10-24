from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse, redirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Student, Teacher, Subject, Staff
from .forms import *
# Create your views here.

def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
        'students': students,
    }
    return render(request, 'base/home.html', context)


@login_required
@user_passes_test(lambda user: user.is_staff)
def dashboard(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    staffs = Staff.objects.all()
    
    female_students = Student.filter_by_gender('F')
    male_students = Student.filter_by_gender('M')

    female_teachers = Teacher.filter_by_gender('F')
    male_teachers = Teacher.filter_by_gender('M')
    
    female_staffs = Staff.filter_by_gender('F')
    male_staffs = Staff.filter_by_gender('M')
    
    context = {
        'teachers': teachers,
        'students': students,
        'staffs': staffs,

        'female_students': female_students,
        'male_students': male_students,

        'female_teachers': female_teachers,
        'male_teachers': male_teachers,

        'female_staffs': female_staffs,
        'male_staffs': male_staffs,
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
            if user.is_staff:
                return redirect('base:dashboard')
            else:
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


@login_required
@user_passes_test(lambda user: user.is_staff)
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = first_name.strip() + '_' + last_name.strip()

            if User.objects.filter(username=username).exists():
                messages.error(request, f'{username} is already registered. Please choose a different username.')
            else:
                user = User.objects.create_user(
                    username=username, 
                    first_name=first_name, 
                    last_name=last_name,
                    email=email,
                    password='@@aa12345',
                )
                if user:
                    name = first_name + ' ' + last_name
                    gender = form.cleaned_data.get('gender')
                    department = form.cleaned_data.get('department')
                    experience = form.cleaned_data.get('experience')
                    phone = form.cleaned_data.get('phone')
                    teacher = Teacher(
                        user=user, 
                        name=name, 
                        gender=gender,
                        department=department, 
                        experience=experience,
                        phone=phone,
                    )
                    if teacher:
                        teacher.save()
                        messages.success(request, f'{name} is registered successfully!')
                    else:
                        user.delete()
                        messages.error(request, 'Someting went wrong while registering Teacher')

                return redirect('base:teacher_register')
            
    else:
        form = TeacherCreationForm()

    context = {
        'form': form,
        'type': 'teacher'
    }
    return render(request, 'dashboard/register.html', context)


@login_required
@user_passes_test(lambda user: user.is_staff)
def student_register(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = first_name.strip() + '_' + last_name.strip()

            if User.objects.filter(username=username).exists():
                messages.error(request, f'{username} is already registered. Please choose a different username.')
            else:
                user = User.objects.create_user(
                    username=username, 
                    first_name=first_name, 
                    last_name=last_name,
                    email=email,
                    password='@@aa12345',
                )
                if user:
                    name = first_name + ' ' + last_name
                    grade = form.cleaned_data.get('grade')
                    age = form.cleaned_data.get('age')
                    gender = form.cleaned_data.get('gender')
                    parent_phone = form.cleaned_data.get('parent_phone')
                    student = Student(
                        user=user, 
                        name=name, 
                        grade=grade, 
                        gender=gender,
                        age=age,
                        parent_phone=parent_phone,
                    )
                    if student:
                        student.save()
                        messages.success(request, f'{name} is registered successfully!')
                    else:
                        user.delete()
                        messages.error(request, 'Someting went wrong while registering Student')
                        
                return redirect('base:student_register')
            
    else:
        form = StudentCreationForm()

    context = {
        'form': form,
        'type': 'student',
    }
    return render(request, 'dashboard/register.html', context)


@login_required
@user_passes_test(lambda user: user.is_staff)
def parent_register(request):
    if request.method == 'POST':
        form = ParentCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = first_name.strip() + '_' + last_name.strip()

            if User.objects.filter(username=username).exists():
                messages.error(request, f'{username} is already registered. Please choose a different username.')
            else:
                user = User.objects.create_user(
                    username=username, 
                    first_name=first_name, 
                    last_name=last_name,
                    email=email,
                    password='@@aa12345',
                )
                if user:
                    name = first_name + ' ' + last_name
                    parent_to = form.cleaned_data.get('parent_to')
                    phone = form.cleaned_data.get('phone')
                    parent = Parent(
                        user=user, 
                        name=name,
                        phone=phone,
                        parent_to=parent_to,
                    )
                    if parent:
                        parent.save()
                        messages.success(request, f'{name} is registered successfully!')
                    else:
                        user.delete()
                        messages.error(request, 'Someting went wrong while registering parent')

                return redirect('base:parent_register')
            
    else:
        form = ParentCreationForm()

    context = {
        'form': form,
        'type': 'parent',
    }
    return render(request, 'dashboard/register.html', context)


@login_required
@user_passes_test(lambda user: user.is_staff)
def staff_register(request):
    if request.method == 'POST':
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = first_name.strip() + '_' + last_name.strip()

            if User.objects.filter(username=username).exists():
                messages.error(request, f'{username} is already registered. Please choose a different username.')
            else:
                user = User.objects.create_user(
                    username=username, 
                    first_name=first_name, 
                    last_name=last_name,
                    email=email,
                    password='@@aa12345',
                    is_staff=True,
                )
                if user:
                    name = first_name + ' ' + last_name
                    gender = form.cleaned_data.get('gender')
                    phone = form.cleaned_data.get('phone')
                    staff = Staff(
                        user=user, 
                        name=name,
                        gender=gender,
                        phone=phone,
                    )
                    if staff:
                        staff.save()
                        messages.success(request, f'{name} is registered successfully!')
                    else:
                        user.delete()
                        messages.error(request, 'Someting went wrong while registering staff')

                return redirect('base:staff_register')
            
    else:
        form = StaffCreationForm()

    context = {
        'form': form,
        'type': 'staff',
    }
    return render(request, 'dashboard/register.html', context)


def restricted_view(request):
    return render(request, 'base/restricted.html')