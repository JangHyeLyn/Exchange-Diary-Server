from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.UserViewSet import UserViewSet
from .views.UserViewSet import UserDetailView
from .views.UserViewSet import UserMeView

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