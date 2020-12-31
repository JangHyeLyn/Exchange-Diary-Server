from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user_view_set import UserViewSet


router = DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
