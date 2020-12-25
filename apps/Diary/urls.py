from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiaryViewSet
router = DefaultRouter()
router.register('diaries', DiaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
