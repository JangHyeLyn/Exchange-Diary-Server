from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.diary_vs import DiaryVS


router = DefaultRouter()
router.register('diaries', DiaryVS)

urlpatterns = [
    path('', include(router.urls)),
]
