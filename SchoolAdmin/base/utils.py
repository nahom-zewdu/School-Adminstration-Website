from django.shortcuts import render, HttpResponse, redirect, HttpResponsePermanentRedirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import *
from .forms import *

import os
from django.core.mail import send_mail
from dotenv import load_dotenv
load_dotenv()

# ###########################################
#      Function to send emails
def send_email(subject, message, recipient):
    send_mail(
        subject=subject, 
        message=message, 
        from_email=os.getenv('EMAIL_HOST_USER'), 
        recipient_list=recipient, 
        fail_silently=True
        )
    print('email sent')
    return True


# ###########################################
#    Functions to publish results according to the class of students
def publish_for_grade_9_and_10(request, sheet, semester, grade):
    complete = []
    success_count = 0
    count = 0
    for row in sheet.iter_rows(min_row=2, values_only=True):
        count += 1
        name = str(row[0]).split()[:2]
        name = ' '.join(name)
        try:
            student = Student.objects.get(name=name, grade=grade)
        except:
            messages.error(request, f'{name} is not a grade {grade} student!')
            continue
        try:
            score_data = {
                'semester': semester,
                'physics': str(row[1]),
                'biology': str(row[2]),
                'chemistry': str(row[3]),
                'average': str(row[4]),
                'rank': str(row[5]),
            }
        except:
            messages.error(request, f'It seems like the fields of {name} are not valid.')
            continue
        
        score_form = PublishScoreForm(score_data)

        if score_form.is_valid():
            if Score.objects.filter(student=student, semester=semester):
                messages.error(request, f'{semester} result for {student} is already set')
                continue
            score = Score(
                student = student,
                semester = semester,
                physics = score_form.cleaned_data['physics'],
                biology = score_form.cleaned_data['biology'],
                chemistry = score_form.cleaned_data['chemistry'],
                average = score_form.cleaned_data['average'],
                rank = score_form.cleaned_data['rank'],
            )
            if score:
                score.save()
                complete.append(score)
                success_count += 1
                if student.parent_set.all():
                    for parent in student.parent_set.all():
                        link = 'http://127.0.0.1:8000/parent_profile/' + parent.parent_id
                        subject = 'MTA students result published'
                        message = f'Hello {parent.name}, \n {semester} result for your child {student.name} is published.'\
                                f'To see the results, go to your profile in the official MTA website or click the link below. \n'\
                                 f'{link}'   
                        send_email(subject=subject, message=message, recipient=[parent.user.email])
                continue
        else:
            messages.error(request, f'Make sure the fields for {row[0]} are all valid!')
    context = {
        'scores': complete,
        'success_count': success_count,
        'count': count,
    }
    return render(request, 'dashboard/score_publish_complete.html', context)


def publish_for_grade_6_to_8(request, sheet, semester, grade):
    complete = []
    success_count = 0
    count = 0
    for row in sheet.iter_rows(min_row=2, values_only=True):
        count += 1
        name = str(row[0]).split()[:2]
        name = ' '.join(name)
        try:
            student = Student.objects.get(name=name, grade=grade)
        except:
            messages.error(request, f'{name} is not a grade {grade} student!')
            continue
        try:
            score_data = {
                'semester': semester,
                'physics': str(row[1]),
                'biology': str(row[2]),
                'chemistry': str(row[3]),
                'average': str(row[4]),
                'rank': str(row[5]),
            }
        except:
            messages.error(request, f'It seems like the fields of {name} are not valid.')
            continue
        
        score_form = PublishScoreForm(score_data)

        if score_form.is_valid():
            if Score.objects.filter(student=student, semester=semester):
                messages.error(request, f'{semester} result for {student} is already set')
                continue
            score = Score(
                student = student,
                semester = semester,
                physics = score_form.cleaned_data['physics'],
                biology = score_form.cleaned_data['biology'],
                chemistry = score_form.cleaned_data['chemistry'],
                average = score_form.cleaned_data['average'],
                rank = score_form.cleaned_data['rank'],
            )
            if score:
                score.save()
                complete.append(score)
                success_count += 1
                if student.parent_set.all():
                    for parent in student.parent_set.all():
                        link = 'http://127.0.0.1:8000/parent_profile/' + parent.parent_id
                        subject = 'MTA students result published'
                        message = f'Hello {parent.name}, \n {semester} result for your child {student.name} is published.'\
                                f'To see the results, go to your profile in the official MTA website or click the link below. \n'\
                                 f'{link}'   
                        send_email(subject=subject, message=message, recipient=[parent.user.email])
                continue
        else:
            messages.error(request, f'Make sure the fields for {row[0]} are all valid!')
    context = {
        'scores': complete,
        'success_count': success_count,
        'count': count,
    }
    return render(request, 'dashboard/score_publish_complete.html', context)


def publish_for_grade_1_to_5(request, sheet, semester, grade):
    complete = []
    success_count = 0
    count = 0
    for row in sheet.iter_rows(min_row=2, values_only=True):
        count += 1
        name = str(row[0]).split()[:2]
        name = ' '.join(name)
        print(name)
        try:
            student = Student.objects.get(name=name, grade=grade)
        except:
            messages.error(request, f'{name} is not a grade {grade} student!')
            continue
        try:
            score_data = {
                'semester': semester,
                'physics': str(row[1]),
                'biology': str(row[2]),
                'chemistry': str(row[3]),
                'average': str(row[4]),
                'rank': str(row[5]),
            }
        except:
            messages.error(request, f'It seems like the fields of {name} are not valid.')
            continue
        
        score_form = PublishScoreForm(score_data)

        if score_form.is_valid():
            if Score.objects.filter(student=student, semester=semester):
                messages.error(request, f'{semester} result for {student} is already set')
                continue
            score = Score(
                student = student,
                semester = semester,
                physics = score_form.cleaned_data['physics'],
                biology = score_form.cleaned_data['biology'],
                chemistry = score_form.cleaned_data['chemistry'],
                average = score_form.cleaned_data['average'],
                rank = score_form.cleaned_data['rank'],
            )
            if score:
                score.save()
                complete.append(score)
                success_count += 1
                if student.parent_set.all():
                    for parent in student.parent_set.all():
                        link = 'http://127.0.0.1:8000/parent_profile/' + parent.parent_id
                        subject = 'MTA students result published'
                        message = f'Hello {parent.name}, \n {semester} result for your child {student.name} is published.'\
                                f'To see the results, go to your profile in the official MTA website or click the link below. \n'\
                                 f'{link}'   
                        send_email(subject=subject, message=message, recipient=[parent.user.email])
                continue
        else:
            messages.error(request, f'Make sure the fields for {row[0]} are all valid!')
    context = {
        'scores': complete,
        'success_count': success_count,
        'count': count,
    }
    return render(request, 'dashboard/score_publish_complete.html', context)