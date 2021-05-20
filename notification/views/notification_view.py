from notification.models import Notification

from rest_framework.generics import ListAPIView

class NotificatoinListView(ListAPIView):
    queryset = Notification.objects.all()


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)