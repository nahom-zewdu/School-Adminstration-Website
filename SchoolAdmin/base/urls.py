from django.urls import path
from . import views

app_name = 'base'


urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),

    path('student_academics/', views.student_academics, name='student_academics'),
    path('teacher_academics/', views.teacher_academics, name='teacher_academics'),
    
    path('restricted/', views.restricted_view, name='restricted'),
    path('student_login/', views.student_login, name='student_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('parent_login/', views.parent_login, name='parent_login'),
    path('logout/', views.logout_view, name='logout'),

    path('student_register/', views.student_register, name='student_register'),
]


