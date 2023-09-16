from django.urls import path
from . import views

app_name = 'base'


urlpatterns = [
    path('', views.home, name="home"),
    path('student_login/', views.student_login, name='student_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('logout/', views.logout_view, name='logout')
]


