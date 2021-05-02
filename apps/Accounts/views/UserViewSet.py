from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404
from ..models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ..permissions import IsSelf
from ..serializers.user_sz import UserSZ
from ..serializers.user_sz import UserUpdateSZ
from django.contrib.auth import get_user_model


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSZ
    http_method_names = ['get','patch','put','delete']
    tags = ["User"]

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action == "create" or self.action == "retrieve":
            permission_classes = [AllowAny]
        elif self.action == "group":
            permission_classes = [AllowAny]
        elif self.action == "hyelyn":
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def me(self, request):
        me = request.user
        serializer = UserSZ(me)
        return Response(data=serializer.data)

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

class UserDetailView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSZ

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)

    def get(self, request, *args, **kwargs):
        request_user = get_object_or_404(User, pk=kwargs['pk'])
        serializer = self.get_serializer(request_user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserMeView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSZ

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(data=serializer.data, status=status.HTTP_200_OK)