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

    @action(methods=['get'], detail=False)
    def my(self, request):
        my_diaries = []
        for member in DiaryMember.objects.filter(user=request.user):
            my_diaries.append(Diary.objects.get(pk=member.diary_id))

        serializer = DiarySZ(my_diaries, many=True)
        return Response(data=serializer.data)

    @action(methods=['get'], detail=True)
    def members(self, request, pk):
        try:
            members = DiaryMember.objects.filter(diary=pk)
            serializer = DiaryMemberSZ(members, many=True)
            return Response(data=serializer.data)
        except DiaryMember.DoesNotExist:
            return Response(data=status.HTTP_400_BAD_REQUEST, status=status.HTTP_400_BAD_REQUEST)

    @members.mapping.post
    def create_member(self, request, pk):
        try:
            diary = Diary.objects.get(pk=pk)
            if DiaryMember.objects.get(diary=diary, user=request.user):
                return Response(status=status.HTTP_226_IM_USED, data=["이미 멤버에 가입되어 있습니다"])

        except DiaryMember.DoesNotExist:
            new_member = DiaryMember.objects.create(
                nickname=request.data.get('nickname', request.user.username),
                diary=diary,
                user=request.user,
            )
            serializer = DiaryMemberSZ(new_member)
            return Response(data=serializer.data)
        except Exception as ex:
            return Response(data=ex, status=status.HTTP_401_UNAUTHORIZED)

    @members.mapping.delete
    def delete_member(self, request, pk):
        """
        TODO::delete 작업 해야됨
        """
        return Response(data=None)
