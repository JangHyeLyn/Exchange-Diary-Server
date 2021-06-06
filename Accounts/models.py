from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(max_length=60, unique=True)
    profile_img = models.ImageField(blank=True, null=True, upload_to="accounts/profile/%Y/%m/%d/%H/%M/%S",
                                help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")
    description = models.CharField(max_length=3000, blank=True, default="안녕하세요")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class UserDisplayName:
    display_name = models.CharField(max_length=100, blank=True, default="name")
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='display_name')
    diary = models.ForeignKey('Diary', on_delete=models.SET_NULL, null=True, related_name='display_name')

    def __str(self):
        return self.user.username