from rest_framework.routers import DefaultRouter
from .views.DiaryViewSet import DiaryViewSet
from .views.DiaryGroupViewSet import DiaryGroupViewSet

router = DefaultRouter()
router.register('diaries', DiaryViewSet)
router.register('diarygroups', DiaryGroupViewSet)
router.register('groups', DiaryGroupViewSet)

urlpatterns = router.urls