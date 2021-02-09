from rest_framework.routers import DefaultRouter
from .views.DiaryViewSet import DiaryViewSet
from .views.DiaryGroupMemberViewSet import DiaryGroupMemberViewSet
from .views.DiaryGroupViewSet import DiaryGroupViewSet

router = DefaultRouter()
router.register('diaries', DiaryViewSet)
router.register('groups', DiaryGroupViewSet)
router.register('groupmembers', DiaryGroupMemberViewSet)

urlpatterns = router.urls