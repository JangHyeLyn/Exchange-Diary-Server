from django.urls import path

from Diary.views.diary_view import DiaryListCreateView
from Diary.views.diary_view import DiaryDetailView
from Diary.views.diary_view import DiaryMeListView
from Diary.views.diary_view import DiaryMemberListCreateView
from Diary.views.diary_view import DiaryMemberMeView
from Diary.views.diary_now_writer_view import DiaryNowWriterView

from Diary.views.diary_group_view import DiaryGroupListCreateUpdateView
from Diary.views.diary_group_view import DiaryGroupDetailView

urlpatterns = [
    # Diary
    path('diaries/', DiaryListCreateView.as_view(), name='diary'),
    path('diaries/<int:pk>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diaries/me/', DiaryMeListView.as_view(), name='diary_me'),
    path('diaries/me/writer/', DiaryNowWriterView.as_view(), name='diary_writer_now_list'),

    # DiaryGroup
    path('diarygroups/', DiaryGroupListCreateUpdateView.as_view(), name='diarygroup'),
    path("diarygroups/<int:pk>/", DiaryGroupDetailView.as_view(), name='diarygroup_detail'),

    # DiaryMember
    path('diaries/<int:diary_pk>/members/', DiaryMemberListCreateView.as_view(), name='diary_member'),
    path('diaries/<int:diary_pk>/members/me/', DiaryMemberMeView.as_view(), name='diary_member_detail'),
]
