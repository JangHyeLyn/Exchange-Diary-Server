from django.db import models

from django.contrib.auth import get_user_model


class Diary(models.Model):
    class MaxPageChoices(models.IntegerChoices):
        LOW, NORMAL, HIGH = 20, 30, 50

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    now_page = models.IntegerField(default=1)
    total_page = models.IntegerField(default=MaxPageChoices.LOW, choices=MaxPageChoices.choices)
    now_writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='now_writer_set')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='diary_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


# class DiaryContent(models.Model):
#    id = models.AutoField(primary_key=True)
#    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='content_set')
#    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='writer_set')
#    content = models.CharField(max_length=300, blank=True)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.content

#    class Meta:
#        ordering = ['-id']

class DiaryMember(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=20, blank=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='member_set')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='writer_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
