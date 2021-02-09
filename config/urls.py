from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # Local Apps
    path('api/v1/', include('Accounts.urls')),
    path('api/v1/', include('Diary.urls')),

    path('account/', include('rest_auth.urls')),
    path('account/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    url(r'account/registration/confirm-email/(?P<key>.+)/$', confirm_email, name='confirm_email'),

    # Kakao Login
    path('', include('KakaoOauth.urls')),

    path('rest-auth/', include('rest_auth.urls')),

]
