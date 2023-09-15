from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def home(request):
    return render(request, 'home.html', {'MTA': 'MTA'})


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