from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model     #returns the User model that is active in these project
from ..models import Teacher


class TeacherAuthBackend(ModelBackend):
    def authenticate(self,request,**kwargs):
        UserMode = get_user_model()
        teacher_id = kwargs.get('teacher_id')
        try:
            teacher = Teacher.objects.get(teacher_id=teacher_id)
        except Teacher.DoesNotExist:
            return None
        else:
            if teacher.user.check_password(kwargs.get('password')):
                return teacher.user
        return None