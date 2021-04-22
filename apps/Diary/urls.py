from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.DiaryViewSet import DiaryViewSet
from .views.DiaryGroupViewSet import DiaryGroupViewSet
from .views.DiaryGroupViewSet import ListCreateDiaryGroupView
from .views.DiaryGroupViewSet import RetrieveDiaryGroupView

# router = DefaultRouter()
# router.register('diaries', DiaryViewSet)
# router.register('diarygroups', ListCreateDiaryGroupView)
# router.register('groups', DiaryGroupViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('diarygroups/', ListCreateDiaryGroupView.as_view(), name='diarygroup'),
    path("diarygroups/<int:pk>/", RetrieveDiaryGroupView.as_view(), name='diarygroup_detail'),
]
