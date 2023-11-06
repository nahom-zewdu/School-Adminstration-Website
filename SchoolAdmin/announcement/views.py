from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .models import *
# Create your views here.

class AnnouncementList(ListView):
    queryset = Announcement.objects.order_by('-timestamp')
    context_object_name = 'announcements'
    template_name = 'announcement/announcement.html'


class DeleteAnnouncement(DeleteView):
    model = Announcement
    context_object_name = 'announcement'
    template_name = 'announcement/delete_announcement.html'
    success_url = reverse_lazy('announcement:announcement')

