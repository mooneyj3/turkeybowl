from django.db import models

from turkeybowl.models.core import Player, Game, TeamPerformance


class TeamStat(models.Model):
    team = models.OneToOneField(TeamPerformance, primary_key=True, on_delete=models.CASCADE)
    totfd = models.IntegerField()
    totyds = models.IntegerField()
    pyds = models.IntegerField()
    ryds = models.IntegerField()
    pen = models.IntegerField()
    penyds = models.IntegerField()
    trnovr = models.IntegerField()
    pt = models.IntegerField()
    ptyds = models.IntegerField()
    ptavg = models.IntegerField()
    top = models.IntegerField()


class PlayerStat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return 'Player Stat: {}'.format(self.player.name)


class Passing(PlayerStat):
    attempts = models.IntegerField()
    completions = models.IntegerField()
    yards = models.IntegerField()
    touchdowns = models.IntegerField()
    interceptions = models.IntegerField()
    two_point_attempts = models.IntegerField()
    two_points_made = models.IntegerField()


class Rushing(PlayerStat):
    attempts = models.IntegerField()
    yards = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()
    two_point_attempts = models.IntegerField()
    two_points_made = models.IntegerField()


class Receiving(PlayerStat):
    receptions = models.IntegerField()
    yards = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()
    two_point_attempts = models.IntegerField()
    two_points_made = models.IntegerField()


class Fumble(PlayerStat):
    total = models.IntegerField()
    recovered = models.IntegerField()
    total_recovered = models.IntegerField()
    yards = models.IntegerField()
    lost = models.IntegerField()


class Kicking(PlayerStat):
    field_goals_made = models.IntegerField()
    field_goal_attempts = models.IntegerField()
    field_goal_yards = models.IntegerField()
    total_field_goal_points = models.IntegerField()
    extra_points_made = models.IntegerField()
    extra_points_missed = models.IntegerField()
    extra_points_attempted = models.IntegerField()
    extra_points_blocked = models.IntegerField()
    extra_points_total = models.IntegerField()


class Punting(PlayerStat):
    punts = models.IntegerField()
    yards = models.IntegerField()
    average = models.IntegerField()
    inside_20_yard_line = models.IntegerField()
    longest = models.IntegerField()


class KickRet(PlayerStat):
    returns = models.IntegerField()
    average = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()


class PuntRet(PlayerStat):
    returns = models.IntegerField()
    average = models.IntegerField()
    touchdowns = models.IntegerField()
    longest = models.IntegerField()
    longest_touchdown = models.IntegerField()


class Defense(PlayerStat):
    tackle = models.IntegerField()
    assisted_tackle = models.IntegerField()
    sack = models.IntegerField()
    interception = models.IntegerField()
    forced_fumble = models.IntegerField()