from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiaryViewSet, DiaryGroupViewSet, DiaryMemberViewSet

router = DefaultRouter()
router.register('diaries', DiaryViewSet)
router.register('groups', DiaryGroupViewSet)
router.register('members', DiaryMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
