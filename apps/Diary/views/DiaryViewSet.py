from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from ..models import Diary, DiaryMember
from ..permissions import IsSelf
from rest_framework.response import Response
from ..serializers.diary_sz import DiarySZ, DiaryDetailSZ
from ..serializers.diary_member_sz import DiaryMemberSZ
from rest_framework import status


class DiaryViewSet(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySZ

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        try:
            diary = self.get_object()
            serializer = DiaryDetailSZ(diary)
            return Response(data=serializer.data)
        except Exception:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=True)
    def join(self, request, pk):
        try:
            member = DiaryMember.objects.create(
                nickname=request.data.get('nickname', request.user.username),
                diary=Diary.objects.get(pk=pk),
                user=request.user
            )
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=DiaryMemberSZ(member).data)

    @join.mapping.delete
    def delete_join(self, request, pk):
        pass

    @action(methods=['get'], detail=False)
    def my(self, request):
        my_diaries = []
        for member in DiaryMember.objects.filter(user=request.user):
            my_diaries.append(Diary.objects.get(pk=member.diary_id))

        serializer = DiarySZ(my_diaries, many=True)
        return Response(data=serializer.data)
