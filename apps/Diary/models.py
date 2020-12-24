from django.db import models

#from apps.Accounts.models import User


#class Diary(models.Model):
#    class MaxPageChoices(models.IntegerChoices):
#        LOW, NORMAL, HIGH = 20, 30, 50

#    id = models.AutoField(primary_key=True)
#    title = models.CharField(max_length=30)
#    now_page = models.IntegerField(default=1)
#    total_page = models.IntegerField(default=MaxPageChoices.LOW, choices=MaxPageChoices.choices)
#    now_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='now_writer')
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.title


#class DiaryContent(models.Model):
#    id = models.AutoField(primary_key=True)
#    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='content')
#    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mycontent')
#    content = models.CharField(max_length=300, blank=True)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.content


#class DiaryMember(models.Model):
#    id = models.AutoField(primary_key=True)
#    nickname = models.CharField(max_length=20, blank=True)
#    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='member')
#    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mydiary')
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.nickname
