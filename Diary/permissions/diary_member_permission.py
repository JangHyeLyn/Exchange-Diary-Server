from rest_framework import permissions

from Diary.models import DiaryMember


class DiaryMemberPermission(permissions.BasePermission):
    """
    Check user is dairy member
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if DiaryMember.objects.filter(diary_id=view.kwargs.get('diary_pk'), user=request.user).exists():
                return True
            return False
        return True
