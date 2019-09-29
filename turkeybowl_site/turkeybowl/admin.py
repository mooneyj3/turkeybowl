# -*- coding: utf-8 -*-
from django.contrib import admin

from turkeybowl.models import *

class TeamPerformanceInline(admin.TabularInline):
    model = TeamPerformance

class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamPerformanceInline,
    ]

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(PlayerStat)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamPerformance)
admin.site.register(Defense)
admin.site.register(Fumble)
admin.site.register(Kicking)
admin.site.register(KickRet)
admin.site.register(Passing)
admin.site.register(Punting)
admin.site.register(PuntRet)
admin.site.register(Receiving)
admin.site.register(Rushing)
admin.site.register(TeamStat)

# Register your models here.
