from ..models import DiaryMember

from rest_framework.generics import CreateAPIView

class DiaryMemberCreateView(CreateAPIView):
    queryset = DiaryMember