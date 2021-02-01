from django.db import models

from django.contrib.auth import get_user_model


class Diary(models.Model):
    class MaxPageChoices(models.IntegerChoices):
        LOW, NORMAL, HIGH = 20, 30, 50

    title = models.CharField(max_length=30)
    now_page = models.IntegerField(default=1)
    total_page = models.IntegerField(default=MaxPageChoices.LOW, choices=MaxPageChoices.choices)
    now_writer = models.ManyToManyField(get_user_model(), related_name='now_writer_set', null=True, blank=True)
    user = models.ManyToManyField(get_user_model(), related_name='diary_set')
    group_join_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class DiaryGroup(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_diary_group_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class DiaryGroupMember(models.Model):
    rank = models.IntegerField()
    group = models.ForeignKey(DiaryGroup, on_delete=models.CASCADE,related_name='group_member_set',null=True, blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE,related_name='group_diary_set', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.diary

    class Meta:
        ordering = ['rank']


# class DiaryContent(models.Model):
#    id = models.AutoField(primary_key=True)
#    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='content')
#    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mycontent')
#    content = models.CharField(max_length=300, blank=True)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.content


class DiaryMember(models.Model):
    nickname = models.CharField(max_length=20, blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='member_set')
    user = models.ManyToManyField(get_user_model(), related_name='mydiary_set', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
