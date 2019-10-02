# -*- coding: utf-8 -*-
from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from nfl_stats.models import *


class StatChildAdmin(PolymorphicChildModelAdmin):
	base_model = Stat


@admin.register(Passing)
class PassingAdmin(StatChildAdmin):
	base_model = Passing


@admin.register(Rushing)
class RushingAdmin(StatChildAdmin):
	base_model = Rushing


@admin.register(Receiving)
class ReceivingAdmin(StatChildAdmin):
	base_model = Receiving


@admin.register(Fumble)
class FumbleAdmin(StatChildAdmin):
	base_model = Fumble


@admin.register(Kicking)
class KickingAdmin(StatChildAdmin):
	base_model = Kicking


@admin.register(Punting)
class PuntingAdmin(StatChildAdmin):
	base_model = Punting


@admin.register(KickRet)
class KickRetAdmin(StatChildAdmin):
	base_model = KickRet


@admin.register(PuntRet)
class PuntRetAdmin(StatChildAdmin):
	base_model = PuntRet


@admin.register(Defense)
class DefenseAdmin(StatChildAdmin):
	base_model = Defense


@admin.register(Stat)
class StatParentAdmin(PolymorphicParentModelAdmin):
	base_model = Stat
	child_models = (
		Passing,
		Rushing,
		Receiving,
		Fumble,
		Kicking,
		Punting,
		KickRet,
		PuntRet,
		Defense,
	)


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)
