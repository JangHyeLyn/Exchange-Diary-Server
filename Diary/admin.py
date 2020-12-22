from django.contrib import admin

from .models import Diary, DiaryContent, DiaryMember


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['title','now_page','total_page','now_writer','created_at','updated_at',]


@admin.register(DiaryContent)
class DiaryContentAdmin(admin.ModelAdmin):
    list_display = []
    pass


@admin.register(DiaryMember)
class DiaryMemberAdmin(admin.ModelAdmin):
    pass
