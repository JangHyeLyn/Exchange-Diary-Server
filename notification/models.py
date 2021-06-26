from django.contrib.contenttypes.models import ContentType
from django.db import models
from core.models.base import BaseModel

from Diary.models import Diary
from Accounts.models import User

from core.models.base import BaseModel


class Notification(BaseModel):
    class TEXT(models.TextChoices):
        INVITE = 'invite', '새로운 일기장에 초대 받았어요!'
        DROP = 'drop', ' 님이 탈퇴하셨습니다.'

    NOTIFICATION_TEXT = (
        '1', '새로운 일기장에 초대 받았어요!',
        '2', ' 님과 교환일기를 작성하러 가볼까요?~?',
        '3', '이제 일기 작성 가능! 초대한 멤버가 들어와서 일기장을 넘겨줄 수 있어요 :)',
        '4', '어서 일기를 작성해주세요! 다른 멤버들이 기다리고 있어요',
        '5', '다음 작성자 지정을 깜박하셨네요! 누구에게 일기장을 넘겨줄까요?',
        '6', ' 님에게 일기장이 넘어왔어요!',
        '7', ' 님이 탈퇴하셨습니다.',
        '8', '!!일기장 임의종료 투표에 참여해주세요.',
        '10', '투표 만장일치로 일기장이 임의종료되었습니다.',
        '11', '일기장을 다 썼네요! 이제 마지막 페이지에서 통계를 확인할 수 있어요!',
        '12', '️1개월 간 작성된 일기가 없어 해당 일기장이 종료될 예정입니다. 종료를 원치 않으시면 3일 이내로 일기를 작성해주세요.',
        '13', '이용하지 않는 일기장이 종료되었습니다.',
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='notifications')
    diary = models.ForeignKey(Diary, on_delete=models.SET_NULL, null=True, related_name='notifications')
    message = models.CharField(max_length=100, choices=TEXT.choices)

    class Meta:
        ordering = ['-pk']

    @classmethod
    def bulk_send_notification(cls, diary, user, text):
        if cls.TEXT.INVITE == text:
            pass
        elif cls.TEXT.DROP == text:
            member_qs = diary.members.all().exclude(user=user)
            message = diary.members.get(user=user).nickname + text.label
            notification_send_list = []
            for member in member_qs:
                notification_drop = Notification(user=member.user, diary=diary, message=message)
                notification_send_list.append(notification_drop)
            cls.objects.bulk_create(notification_send_list)
            return None
