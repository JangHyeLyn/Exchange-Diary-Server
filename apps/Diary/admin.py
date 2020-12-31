from django.contrib import admin

from .models import Diary, DiaryMember  # DiaryContent,


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['title', 'now_page', 'total_page', 'now_writer', 'created_at', 'updated_at', ]


# @admin.register(DiaryContent)
# class DiaryContentAdmin(admin.ModelAdmin):
#    list_display = ['diary','writer','content','created_at','updated_at']


@admin.register(DiaryMember)
class DiaryMemberAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'diary', 'user', 'created_at', 'updated_at']
