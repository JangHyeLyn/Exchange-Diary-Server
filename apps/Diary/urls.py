from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.DiaryViewSet import DiaryViewSet
from .views.DiaryGroupMemberViewSet import DiaryGroupMemberViewSet
from .views.DiaryMemberViewSet import DiaryMemberViewSet
from .views.DiaryGroupViewSet import DiaryGroupViewSet

router = DefaultRouter()
router.register('diaries', DiaryViewSet)
router.register('groups', DiaryGroupViewSet)
router.register('members', DiaryMemberViewSet)
router.register('groupmembers', DiaryGroupMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
