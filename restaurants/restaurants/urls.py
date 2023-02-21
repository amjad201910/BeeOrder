from django.urls import path,include,re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import  PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password-reset-confirm/<uidb64>/<tokens>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

      re_path(r'registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
      re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),

                  #####################################################
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

##################   ################################################3

                  path('restaurant/', include('restaurant.urls')),
                  path('user/', include('user.urls')),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
