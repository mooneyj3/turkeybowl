from django.db import models
from polymorphic.models import PolymorphicModel


class Team(models.Model):
    abbreviation = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return('{} {}'.format(self.abbreviation, self.name))


class Player(models.Model):
    player_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

    def __str__(self):
        return(self.name)


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_team', on_delete=models.DO_NOTHING)
    away_team = models.ForeignKey(Team, related_name='away_team', on_delete=models.DO_NOTHING)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return('{} vs. {}, {}'.format(self.home_team, self.away_team, self.date))


class Stat(PolymorphicModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.__class__.__name__, self.player.name, self.game.__str__())


class Passing(Stat):
    stat_type = models.CharField(max_length=20, default='passing')
    attempts = models.IntegerField()
    completions = models.IntegerField()
    yards = models.IntegerField()
    touchdowns = models.IntegerField()
    interceptions = models.IntegerField()
    two_point_attempts = models.IntegerField()
    two_points_made = models.IntegerField()


class Rushing(Stat):
    stat_type = models.CharField(max_length=20, default='rushing')
    attempts = models.IntegerField()
    yards = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()
    two_point_attempts = models.IntegerField()
    two_points_made = models.IntegerField()


class Receiving(Stat):
    stat_type = models.CharField(max_length=20, default='receiving')
    receptions = models.IntegerField()
    yards = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()
    two_point_attempts = models.IntegerField()
    two_points_made = models.IntegerField()


class Fumble(Stat):
    stat_type = models.CharField(max_length=20, default='fumble')
    total = models.IntegerField()
    recovered = models.IntegerField()
    total_recovered = models.IntegerField()
    yards = models.IntegerField()
    lost = models.IntegerField()


class Kicking(Stat):
    stat_type = models.CharField(max_length=20, default='kicking')
    field_goals_made = models.IntegerField()
    field_goal_attempts = models.IntegerField()
    field_goal_yards = models.IntegerField()
    total_field_goal_points = models.IntegerField()
    extra_points_made = models.IntegerField()
    extra_points_missed = models.IntegerField()
    extra_points_attempted = models.IntegerField()
    extra_points_blocked = models.IntegerField()
    extra_points_total = models.IntegerField()


class Punting(Stat):
    stat_type = models.CharField(max_length=20, default='punting')
    punts = models.IntegerField()
    yards = models.IntegerField()
    average = models.IntegerField()
    inside_20_yard_line = models.IntegerField()
    longest = models.IntegerField()


class KickRet(Stat):
    stat_type = models.CharField(max_length=20, default='kick_return')
    returns = models.IntegerField()
    average = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()


class PuntRet(Stat):
    stat_type = models.CharField(max_length=20, default='punt_return')
    returns = models.IntegerField()
    average = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()


class Defense(Stat):
    stat_type = models.CharField(max_length=20, default='defense')
    tackle = models.IntegerField()
    assisted_tackle = models.IntegerField()
    sack = models.IntegerField()
    interception = models.IntegerField()
    forced_fumble = models.IntegerField()