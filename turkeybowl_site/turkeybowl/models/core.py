# -*- coding: utf-8 -*-
from django.db import models


class Team(models.Model):
    abbr = models.CharField(max_length=5, primary_key=True)

    def __str__(self):
        return self.abbr


class TeamPerformance(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score_1 = models.IntegerField()
    score_2 = models.IntegerField()
    score_3 = models.IntegerField()
    score_4 = models.IntegerField()
    score_5 = models.IntegerField()
    score_T = models.IntegerField()
    to = models.IntegerField()

    def __str__(self):
        return self.team.abbr


class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    home_team_perf = models.OneToOneField(TeamPerformance, related_name='home_team', on_delete=models.CASCADE)
    away_team_perf = models.OneToOneField(TeamPerformance, related_name='away_team', on_delete=models.CASCADE)
    weather = models.CharField(max_length=50)
    media = models.CharField(max_length=50)
    yardline = models.IntegerField()
    quarter = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    down = models.IntegerField()
    togo = models.IntegerField()
    redzone = models.BooleanField()
    clock = models.CharField(max_length=50)
    posteam = models.CharField(max_length=50)
    stadium = models.CharField(max_length=50)

    def __str__(self):
        return '{} vs. {}'.format(self.home_team_perf.team.abbr, self.away_team_perf.team.abbr)


class Player(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
