from .models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsSelf
from .serializers import UserSZ
from django.contrib.auth import get_user_model


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSZ

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif self.action == "create" or self.action == "retrieve":
            permission_classes = [AllowAny]
        elif self.action == "group":
            permission_classes = [IsSelf]
        elif self.action == "hyelyn":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def me(self, request):
        me = request.user
        serializer = UserSZ(me)
        return Response(data=serializer.data)

    @action(detail=True)
    def group(self, request, pk):
        return Response(data="123123123")

    @action(detail=False, methods=['get'])
    def hyelyn(self, request):
        hyelyn = User.objects.get(email="nfzoze01@gmail.com")
        serializer = UserSZ(hyelyn)
        return Response(data=serializer.data)

    @hyelyn.mapping.patch
    def put_hyelyn(self, request):
        hyelyn = User.objects.get(email="nfzoze01@gmail.com")
        serializer = UserSZ(hyelyn, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)