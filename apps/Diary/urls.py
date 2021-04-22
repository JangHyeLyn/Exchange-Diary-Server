from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.DiaryViewSet import DiaryViewSet
from .views.DiaryGroupViewSet import DiaryGroupViewSet,ListCreateDiaryGroupView

router = DefaultRouter()
router.register('diaries', DiaryViewSet)
router.register('diarygroups', ListCreateDiaryGroupView)
# router.register('groups', DiaryGroupViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path("dddd/",ListCreateDiaryGroupView.as_view(), name='diarygroup'),
]