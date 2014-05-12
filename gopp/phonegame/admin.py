# This Python file uses the following encoding: utf-8
from django.contrib import admin
from phonegame.models import gameinfo,companyinfo
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
# Register your models here.
class GamesInline(admin.TabularInline):
    model = gameinfo
    readonly_fields = ('appkey',)
    extra = 1


class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        ('厂商信息', {'fields':['company']}),
        ('时间信息',{'fields':['ccreatedate'],'classes':['collapse']}),
        ('详细信息',{'fields':['companyid','crating','cvotes']})
    ]
    inlines = [GamesInline]
    list_display = ('company','companyid','crating','cvotes')
    # list_filter = ['createdate']
    search_fields = ['gameinfo__gamename']

admin.site.register(companyinfo,GameAdmin)


class GInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('appkey',)

    list_display = ('gamename','gcreatedate','gameid','grating','gvotes','appkey')

admin.site.register(gameinfo,GInfoAdmin)