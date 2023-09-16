from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model     #returns the User model that is active in these project
from ..models import Parent


class ParentAuthBackend(ModelBackend):
    def authenticate(self,request,**kwargs):
        UserMode = get_user_model()
        parent_id = kwargs.get('parent_id')
        try:
            parent = Parent.objects.get(parent_id=parent_id)
        except Parent.DoesNotExist:
            return None
        else:
            if parent.user.check_password(kwargs.get('password')):
                return parent.user
        return None