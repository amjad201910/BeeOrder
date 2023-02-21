


from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.urls import exceptions as url_exceptions
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

#from dj_rest_auth.app_settings import api_settings

UserModel = get_user_model()

if 'allauth' in settings.INSTALLED_APPS:
    from dj_rest_auth.forms import AllAuthPasswordResetForm

from dj_rest_auth.models import TokenModel
#######################################change password

from dj_rest_auth.serializers import PasswordChangeSerializer,PasswordResetConfirmSerializer

class SetPasswordForm2(SetPasswordForm):
    def __init__(self,user, *args,**kwargs):


        super().__init__(user, *args,**kwargs)
        self.fields.pop('new_password2')



class PasswordChangeSerializer2(PasswordChangeSerializer):
    set_password_form_class=SetPasswordForm2
    def __init__(self, *args, **kwargs):
        self.fields.pop('new_password2')

        super().__init__(*args, **kwargs)









##########################################forgate password
class PasswordResetConfirmSerializer2(PasswordResetConfirmSerializer):
    set_password_form_class=SetPasswordForm2


    def __init__(self, *args, **kwargs):
        self.fields.pop('new_password2')
        super().__init__(*args, **kwargs)
