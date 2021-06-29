from django.contrib import admin

from .models import Diary, DiaryMember, DiaryGroup   # , DiaryContent


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['title', 'now_page', 'total_page', 'created_at', 'updated_at', ]


@admin.register(DiaryGroup)
class DiaryGroupAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'user']
    ordering = ['-pk']

# @admin.register(DiaryGroupMember)
# class DiaryGroupMember(admin.ModelAdmin):
#     pass

# @admin.register(DiaryContent)
# class DiaryContentAdmin(admin.ModelAdmin):
#    list_display = ['diary','writer','content','created_at','updated_at']


@admin.register(DiaryMember)
class DiaryMemberAdmin(admin.ModelAdmin):
    list_display = ['nickname','diary', 'created_at', 'updated_at']
