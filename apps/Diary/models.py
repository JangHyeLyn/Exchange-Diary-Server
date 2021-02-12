from django.db import models

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
    now_writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='now_writers')
    master = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='diaries')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class DiaryMember(BaseModel):
    nickname = models.CharField(max_length=20, blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='joins')

    def __str__(self):
        return self.nickname

class DiaryGroup(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_diary_group_set')
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['rank']

class DiaryGroupMember(BaseModel):
    rank = models.IntegerField()
    group = models.ForeignKey(DiaryGroup, on_delete=models.CASCADE,related_name='members',null=True, blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE,related_name='group', blank=True, null=True)

    def __str__(self):
        return str(self.rank)

    class Meta:
        ordering = ['rank']


