from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.user_view import UserViewSet
from .views.user_view import UserDetailView
from .views.user_view import UserMeView

app_name = 'Accounts'
# router = DefaultRouter()
# router.register('users', UserViewSet)

# urlpatterns = router.urls

urlpatterns = [
    #user
    # path('users/', UserDetailView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/me/', UserMeView.as_view(), name='user_me'),
]