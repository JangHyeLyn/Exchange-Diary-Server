from django.db import models, transaction

from django.contrib.auth import get_user_model

from core.models.base import BaseModel


class Diary(BaseModel):
    class Status(models.TextChoices):
        READY = (0, 'ready')
        ING = (1, 'ing')
        FINISH = (2, 'finish')

    title = models.CharField(max_length=30)
    now_page = models.IntegerField(default=1)
    total_page = models.IntegerField(default=20)
    _now_writer = models.ForeignKey(get_user_model(), db_column='now_writer_id', on_delete=models.SET_NULL, null=True,
                                    related_name='now_writers')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='diaries')
    cover = models.IntegerField(default=1)
    promise = models.CharField(max_length=500, null=True, blank=True)
    group = models.ForeignKey('DiaryGroup', default=None, on_delete=models.SET_NULL, null=True, related_name='diaries')
    status = models.IntegerField(default=0)  # 0 - ready , 1 - ing , 2 - finish

    # TODO: 다이어리 상태 정의 해야됨 choice fields로 정의서 받으면 그때 진행
    # status = models.
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.pk}-{self.title}'

    @property
    def now_writer(self):
        try:
            now_writer_list = list(self.members.filter(user=self._now_writer).values_list('nickname', flat=True))
            now_writer = now_writer_list.pop()
            return now_writer
        except Exception as e:
            return None

    @now_writer.setter
    def now_writer(self, value):
        self._now_writer = value


class DiaryMember(BaseModel):
    nickname = models.CharField(max_length=20, blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null=True, related_name='members')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='joins')
    profile_img = models.ImageField(null=True, upload_to="accounts/profile/%Y/%m/%d/%H/%M/%S",
                                    help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")

    def __str__(self):
        return self.nickname


class DiaryGroup(BaseModel):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True,
                             related_name='user_diary_group_set')
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['rank']

    @classmethod
    def group_count(cls, pk):
        return cls.objects.prefetch_related('diaries').get(pk=pk).diaries.count()

    @staticmethod
    def not_join_group_count(user):
        return Diary.objects.filter(user=user, group__isnull=True).count()

    @classmethod
    def group_rank_update(cls, datas):
        for data in datas:
            DiaryGroup.objects.filter(pk=data.get('id')).update(rank=data.get('rank'))

    @classmethod
    def get_next_group_rank(cls, user):
        if cls.objects.filter(user=user):
            return cls.objects.filter(user=user).last().rank + 1
        return 1
