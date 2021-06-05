from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views.diaryview import DiaryViewSet
from .views.diary_view import DiaryListCreateView
from .views.diary_view import DiaryDetailView
from .views.diary_view import DiaryMeListView
from .views.diary_view import DiaryMemberListCreateView
from .views.diary_view import DiaryMemberDetailView

from .views.diary_group_view import DiaryGroupViewSet
from .views.diary_group_view import DiaryGroupListCreateUpdateView
from .views.diary_group_view import DiaryGroupDetailView


# router = DefaultRouter()
# router.register('diaries', DiaryViewSet)
# router.register('diarygroups', ListCreateDiaryGroupView)
# router.register('groups', DiaryGroupViewSet)

# urlpatterns = router.urls
urlpatterns = [
    # Diary
    path('diaries/', DiaryListCreateView.as_view(), name='diary'),
    path('diaries/<int:pk>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diaries/me/', DiaryMeListView.as_view(), name='diary_me'),

    # DiaryGroup
    path('diarygroups/', DiaryGroupListCreateUpdateView.as_view(), name='diarygroup'),
    path("diarygroups/<int:pk>/", DiaryGroupDetailView.as_view(), name='diarygroup_detail'),

    # DiaryMember
    path('diaries/<int:pk>/members/', DiaryMemberListCreateView.as_view(), name='diary_member'),
    path('diaries/<int:diary_pk/members/<int:pk>/', DiaryMemberDetailView.as_view(), name='diary_member_detail'),
]
