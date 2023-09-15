from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model     #returns the User model that is active in these project
from ..models import Student


class StudentAuthBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        UserModel = get_user_model()
        student_id = kwargs.get('student_id')

        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            return None
        else:
            if student.user.check_password(kwargs.get('password')):
                return student.user
        
        return None
