from django.db import models, transaction

from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Diary(BaseModel):
    title = models.CharField(max_length=30)
    now_page = models.IntegerField(default=1)
    total_page = models.IntegerField(default=20)
    now_writer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='now_writers')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='diaries')
    cover = models.IntegerField(default=1)
    promise = models.CharField(max_length=500, null=True, blank=True)

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
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='user_diary_group_set')
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['rank']

    @classmethod
    def group_count(cls, pk):
        group = DiaryGroup.objects.get(pk=pk)
        group_member_count = group.members.all().count()
        return group_member_count

    @classmethod
    def not_join_group_count(cls, user):
        return Diary.objects.filter(user=user, group__isnull=True).count()

    @classmethod
    @transaction.atomic()
    def group_rank_update(cls, datas):
        for data in datas:
            group = DiaryGroup.objects.get(pk=data.get('id'))
            group.rank = data.get('rank')
            group.save()


class DiaryGroupMember(BaseModel):
    group = models.ForeignKey(DiaryGroup, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.SET_NULL, null=True, related_name='group', blank=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.diary.title
