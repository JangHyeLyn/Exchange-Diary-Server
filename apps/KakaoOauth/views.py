from config.settings.secret import SECRET
from django.shortcuts import redirect, render
import requests
import json

from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


# code 요청
def kakao_login(request):
    app_rest_api_key = SECRET['SOCIALACCOUNT_PROVIDERS']['kakao']['APP']['client_id']
    redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


# access token 요청
def kakao_callback(request):
    redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback"
    kakao_access_token_request_uri = "https://kauth.kakao.com/oauth/token"
    request_data = {
        'grant_type': 'authorization_code',
        'client_id': SECRET['SOCIALACCOUNT_PROVIDERS']['kakao']['APP']['client_id'],
        'redirect_uri': redirect_uri,
        'code': request.GET.get('code')
    }
    response_json = json.loads(requests.post(kakao_access_token_request_uri, data=request_data).content)
    access_token = response_json['access_token']

    print(access_token)
    user_get_uri = 'https://kapi.kakao.com/v2/user/me'
    header = {'Authorization': f'Bearer {access_token}'}
    user_data = requests.post(user_get_uri, headers=header)

    user_data = user_data.json()
    print(user_data)
    return render(request, 'index.html', {
        'access_token': access_token
    })

#from rest_framework_jwt.
class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

