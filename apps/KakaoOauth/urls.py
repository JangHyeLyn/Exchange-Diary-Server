from django.urls import path
from .views import kakao_callback, kakao_login, KakaoLogin

app_name = 'KakaoOauth'

urlpatterns = [
    path('account/login/kakao/', kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),

    # All-Auth
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
]