from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.diaryview import DiaryViewSet
from .views.diarygroupview import DiaryGroupViewSet
from .views.diarygroupview import ListCreateDiaryGroupView
from .views.diarygroupview import DiaryGroupDetailView

# router = DefaultRouter()
# router.register('diaries', DiaryViewSet)
# router.register('diarygroups', ListCreateDiaryGroupView)
# router.register('groups', DiaryGroupViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('diarygroups/', ListCreateDiaryGroupView.as_view(), name='diarygroup'),
    path("diarygroups/<int:pk>/", DiaryGroupDetailView.as_view(), name='diarygroup_detail'),
]
