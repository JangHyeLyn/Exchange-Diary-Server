from django.db import transaction
from django.views import View
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status, viewsets, mixins
from ..models import Diary, DiaryMember, DiaryGroup, DiaryGroupMember
from ..permissions import IsSelf
from rest_framework.response import Response
from ..serializers.diary_sz import DiarySZ, DiaryDetailSZ
from ..serializers.diary_member_sz import DiaryMemberSZ
from ..serializers.diary_group_sz import DiaryGroupListSZ
from ..serializers.diary_group_member_sz import DiaryGroupMemberSZ
from ..serializers.diary_group_id_sz import DiaryGroupIdSZ
from rest_framework import status

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class DiaryListCreateView(ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySZ
    # permission_classes = (
    #     IsAuthenticated,
    # )

    def get_queryset(self):
        return Diary.objects.filter(user=self.request.user)

    # @transaction.atomic()
    # def post(self, request, *args, **kwargs):
    #
    #     pass

class DiaryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiaryDetailSZ
    permission_classes = (
        IsAuthenticated,
    )

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DiaryViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   View):
    '''
    다이어리 관련

    다이어리 관련
    '''
    queryset = Diary.objects.all()
    serializer_class = DiarySZ
    tags = ["Diary"]

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action == "delete":
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        '''
        다이어리 상세 정보 조회

        다이어리의 상세 정보를 조회
        '''
        try:
            diary = self.get_object()
            serializer = DiaryDetailSZ(diary)
            return Response(data=serializer.data)
        except Exception:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False)
    def my(self, request):
        '''
        내가 가입한 다이어리 확인

        내가 가입한 다이어리 확인 pk없이 jwt만 있으면 확인 가능
        '''

        # 나의 다이어리 가지고오는 orm 수
        # my_diaries = []
        # for member in DiaryMember.objects.filter(user=2):
        #     my_diaries.append(Diary.objects.get(pk=member.diary_id))

        my_diaries = Diary.objects.filter(members__user=request.user)

        serializer = DiarySZ(my_diaries, many=True)
        return Response(data=serializer.data)

    @action(methods=['get'], detail=True)
    def members(self, request, pk):
        '''
        현재 다이어리에 속해있는 유저 정보 확인

        현재 다이어리에 누가 있는지 확인
        '''
        try:
            members = DiaryMember.objects.filter(diary=pk)
            serializer = DiaryMemberSZ(members, many=True)
            return Response(data=serializer.data)
        except DiaryMember.DoesNotExist:
            return Response(data=status.HTTP_400_BAD_REQUEST, status=status.HTTP_400_BAD_REQUEST)

    @members.mapping.post
    def create_member(self, request, pk):
        '''
        다이어리에 가입

        다이어리에 새로 참여하게 되면 가입시 이름이 아닌 닉네임을 사용하기로\n
        했기 때문에 다이어리에 가입하려면 닉네임을 작성해야 된다\n

        현재 다이어리 생성 부터 가입 까지의 로직은 아래와 같다\n
        다이어리를 생성한 사람은 다이어리를 생성함으로써 다이어리에 가입이 되는것이 아니다\n
        닉네임을 동반하여 다이어리 멤버에 가입을 해야지만 최종적으로 다이어리에 가입이 되는것 이다.\n
        '''

        if Diary.objects.filter(members__diary=pk).filter(members__user=request.user):
            return Response(data=["이미 멤버에 가입되어 있습니다"])
        else:
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

    @members.mapping.delete
    def delete_member(self, request, pk):
        """
        다이어리 멤버 삭제

        작업 예정
        TODO::delete 작업 해야됨
        """
        return Response(data=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def group(self, request, pk):
        '''
        특정 다이어리에서 그룹 가입 여부 확인

        다이어리안에서 사용자가 만든 그룹을 볼수 있고\n
        현재 다이어리가 어느 그룹에 속해 있는지 확인\n
        is_group가 True이면 그룹에 속해 있다는 것\n
        is_group가 False이면 그룹에 속해 있지 않다는 것\n
        모든 그룹에 대해 is_group가 False이면 미지정 그룹에 속해있는것
        '''
        # pk는 diary의 pk이다.
        my_group = DiaryGroup.objects.filter(user=request.user)
        group_serializer = DiaryGroupListSZ(my_group, many=True, context={'request': request, 'diary_pk': pk})

        return Response(data=group_serializer.data)

    @group.mapping.post
    def add_group_member(self, request, pk):
        '''
        현재 다이어리의 그룹을 변경

        현재 가입되어 있는 다이어리 그룹을 변경
        '''
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
                print("에러발생")
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
