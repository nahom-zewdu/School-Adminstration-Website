from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
app_name = 'announcement'

urlpatterns = [
    path('', views.AnnouncementList.as_view(), name='announcement'),
    path('delete_announcement/<int:pk>', views.DeleteAnnouncement.as_view(), name='delete_announcement'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
