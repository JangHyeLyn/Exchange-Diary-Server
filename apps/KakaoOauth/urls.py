from django.urls import path
from .views import kakao_callback,kakao_login

urlpatterns = [
    path('account/login/kakao/', kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),
]