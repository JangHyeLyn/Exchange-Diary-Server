from django.db import models, transaction

from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Diary(BaseModel):
    # STATUS_CHOICE = {
    #     ("0" : ""),
    #     ("1" : "")
    # }
    title = models.CharField(max_length=30)
    now_page = models.IntegerField(default=1)
    total_page = models.IntegerField(default=20)
    now_writer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='now_writers')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='diaries')
    cover = models.IntegerField(default=1)
    promise = models.CharField(max_length=500, null=True, blank=True)
    group = models.ForeignKey('DiaryGroup', default=None, on_delete=models.SET_NULL, null=True, related_name='diaries')
    # TODO: 다이어리 상태 정의 해야됨 choice fields로 정의서 받으면 그때 진행
    # status = models.

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class DiaryMember(BaseModel):
    nickname = models.CharField(max_length=20, blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null=True, related_name='members')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='joins')

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

# class DiaryGroupMember(BaseModel):
#     group = models.ForeignKey(DiaryGroup, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
#     diary = models.ForeignKey(Diary, on_delete=models.SET_NULL, null=True, related_name='groupqwer', blank=True)
#
#     class Meta:
#         ordering = ['pk']
#
#     def __str__(self):
#         return self.diary.title
