from django.db import models
from base.models import *
# Create your models here.


class Announcement(models.Model):
    creator = models.ForeignKey(Staff, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title