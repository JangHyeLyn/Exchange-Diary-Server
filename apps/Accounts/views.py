from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import UserSZ
from django.contrib.auth import get_user_model

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSZ
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(
            Q(email=self.request.user.email)
        )
        return qs
#class UserDetailViewSet(ModelViewSet):
#    queryset = User.objects