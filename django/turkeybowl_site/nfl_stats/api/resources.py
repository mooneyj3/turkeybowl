from django.db.models import ForeignKey, OneToOneField

from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from nfl_stats.models import *


class TeamResource(ModelResource):
	class Meta:
		queryset = Team.objects.all()
		resource_name = 'team'


class PlayerResource(ModelResource):
	team = fields.ForeignKey(TeamResource, 'team', full=True)

	class Meta:
		queryset = Player.objects.all()
		resource_name = 'player'


class GameResource(ModelResource):
	home_team = fields.ForeignKey(TeamResource, 'home_team', full=True)
	away_team = fields.ForeignKey(TeamResource, 'away_team', full=True)

	class Meta:
		queryset = Game.objects.all()
		resource_name = 'game'


class StatResource(ModelResource):
	game = fields.ForeignKey(GameResource, 'game', full=True)
	player = fields.ForeignKey(PlayerResource, 'player', full=True)

	class Meta:
		queryset = Stat.objects.all()
		resource_name = 'stat'

	def dehydrate(self, bundle):
		unacceptable_field_types = (ForeignKey, OneToOneField)

		for field in bundle.obj._meta.fields:
			if field.name in bundle.data:
				continue
			if not isinstance(field, unacceptable_field_types):
				bundle.data[field.name] = getattr(bundle.obj, field.name)

		return bundle.data
