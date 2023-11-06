from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import CreateView, ListView, DetailView, DeleteView

from .models import *
from .forms import *
# Create your views here.

class AnnouncementList(LoginRequiredMixin, ListView):
    queryset = Announcement.objects.order_by('-timestamp')
    context_object_name = 'announcements'
    template_name = 'announcement/announcement.html'

    login_url = '/restricted/'

class CreateAnnouncement(CreateView, LoginRequiredMixin):
    model = Announcement
    form_class = AnnouncementCreationForm
    template_name = 'announcement/create_announcement.html'
    success_url = reverse_lazy('announcement:announcement')

    login_url = '/restricted/'

    def form_valid(self, form):
        form.instance.creator = self.request.user.staff

        return super().form_valid(form)

class DeleteAnnouncement(DeleteView, LoginRequiredMixin):
    model = Announcement
    context_object_name = 'announcement'
    template_name = 'announcement/delete_announcement.html'
    success_url = reverse_lazy('announcement:announcement')

    login_url = '/restricted/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Announcement deleted successfully.')
        return super().delete(request, *args, **kwargs)
