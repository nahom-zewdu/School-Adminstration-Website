from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model     #returns the User model that is active in these project
from ..models import Staff


class StaffAuthBackend(ModelBackend):
    def authenticate(self,request,**kwargs):
        UserMode = get_user_model()
        staff_id = kwargs.get('staff_id')
        try:
            staff = Staff.objects.get(staff_id=staff_id)
        except Staff.DoesNotExist:
            return None
        else:
            if staff.user.check_password(kwargs.get('password')):
                return staff.user
        return None