from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60, unique=True)
    profile = models.ImageField(blank=True, upload_to="accounts/profile/%Y/%m/%d/%H/%M/%S",
                                help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")

    description = models.CharField(max_length=50, blank=True, default="안녕하세요")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
