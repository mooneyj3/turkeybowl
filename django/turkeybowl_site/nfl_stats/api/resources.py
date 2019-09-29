from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from nfl_stats.models import *


class TeamResource(ModelResource):
	class Meta:
		queryset = Team.objects.all()
		resource_name = 'team'


class TeamPerformanceResource(ModelResource):
	team = fields.ForeignKey(TeamResource, 'team', full=True)

	class Meta:
		queryset = TeamPerformance.objects.all()
		resource_name = 'team_performance'


class GameResource(ModelResource):
	home_team = fields.OneToOneField(TeamPerformanceResource, 'home_team_perf', full=True)
	away_team = fields.OneToOneField(TeamPerformanceResource, 'away_team_perf', full=True)

	class Meta:
		queryset = Game.objects.all()
		resource_name = 'game'


class PlayerResource(ModelResource):
	class Meta:
		queryset = Player.objects.all()
		resource_name = 'player'


class TeamStatResource(ModelResource):
	team = fields.OneToOneField(TeamResource, 'team', full=True)

	class Meta:
		queryset = TeamStat.objects.all()
		resource_name = 'team_stat'


class PlayerStatResource(ModelResource):
	player = fields.ForeignKey(TeamResource, 'player', full=True)

	class Meta:
		queryset = PlayerStat.objects.all()
		resource_name = 'player_stat'