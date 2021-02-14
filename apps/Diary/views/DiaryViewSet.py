from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from ..models import Diary, DiaryMember, DiaryGroup, DiaryGroupMember
from ..permissions import IsSelf
from rest_framework.response import Response
from ..serializers.diary_sz import DiarySZ, DiaryDetailSZ
from ..serializers.diary_member_sz import DiaryMemberSZ
from ..serializers.diary_group_sz import DiaryGroupSZ
from ..serializers.diary_group_member_sz import DiaryGroupMemberSZ
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
                return Response(data=["이미 멤버에 가입되어 있습니다"])

        except DiaryMember.DoesNotExist:
            data = {
                'nickname': request.data.get('nickname', request.user.username),
                'diary': pk,
            }

            serializer = DiaryMemberSZ(data=data, context=request)
            if serializer.is_valid():
                new_member = serializer.save()
                return Response(data=DiaryMemberSZ(new_member).data)
            else:
                return Response(data=serializer.errors)
        except Exception as ex:
            return Response(data=ex, status=status.HTTP_401_UNAUTHORIZED)

    @members.mapping.delete
    def delete_member(self, request, pk):
        """
        TODO::delete 작업 해야됨
        """
        return Response(data=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def group(self, request, pk):
        # pk는 diary의 pk이다.
        my_group = DiaryGroup.objects.filter(user=request.user)
        group_serializer = DiaryGroupSZ(my_group, many=True)
        is_member = DiaryGroupMember.objects.filter(diary=pk)
        content = {
            'group': group_serializer.data,
        }

        # 다이어리가 그룹안에 포함되어 있을때
        if is_member:
            content['is_group'] = is_member.first().group.id

        # 다이어가 그룹안에 포함되어 있지 않을 때
        else:
            content['is_group'] = 0

        return Response(data=content)

    @group.mapping.post
    def add_group_member(self, request, pk):
        member = DiaryGroupMember.objects.filter(diary=pk)

        # 그룹에 속해 있다면
        if member:
            member.delete()
        # 미 지정 그룹
        if request.data.get('group') == 0:
            return Response(data={'group': 0})
        # 지정 그룹
        else:
            data = {
                'rank': 1,
                'group': request.data.get('group'),
                'diary': pk,
            }

            serializer = DiaryGroupMemberSZ(data=data, context=request)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'group': request.data.get('group')})
            else:
                return Response(data=serializer.errors)