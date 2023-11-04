from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class AnnouncementList(ListView):
    queryset = Announcement.objects.order_by('-timestamp')
    context_object_name = 'announcements'
    template_name = 'announcement/announcement.html'
