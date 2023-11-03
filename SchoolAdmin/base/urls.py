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
    path('teacher_register/', views.teacher_register, name='teacher_register'),
    path('parent_register/', views.parent_register, name='parent_register'),
    path('staff_register/', views.staff_register, name='staff_register'),


    path('student_register_with_file/', views.student_register_with_file, name='student_register_with_file'),
    path('teacher_register_with_file/', views.teacher_register_with_file, name='teacher_register_with_file'),

    path('student_dashboard/<str:grade>', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('parent_dashboard/', views.parent_dashboard, name='parent_dashboard'),


    path('result_dashboard/<str:grade>', views.result_dashboard, name='result_dashboard'),
    path('publish_result/', views.publish_result, name='publish_result'),


    path('student_update/<str:pk>', views.student_update, name='student_update'),
    path('teacher_update/<str:pk>', views.teacher_update, name='teacher_update'),
    path('parent_update/<str:pk>', views.parent_update, name='parent_update'),
    path('staff_update/<str:pk>', views.staff_update, name='staff_update'),


    path('student_profile/<str:pk>', views.student_profile, name='student_profile'),
    path('parent_profile/<str:pk>', views.parent_profile, name='parent_profile'),

    path('change_password', views.change_password, name='change_password'),
]


