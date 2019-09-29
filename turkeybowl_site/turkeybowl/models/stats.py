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
    att = models.IntegerField()
    cmp = models.IntegerField()
    yards = models.IntegerField()
    touchdowns = models.IntegerField()
    interceptions = models.IntegerField()
    twopta = models.IntegerField()
    twoptm = models.IntegerField()


class Rushing(PlayerStat):
    att = models.IntegerField()
    yds = models.IntegerField()
    tds = models.IntegerField()
    lng = models.IntegerField()
    lngtd = models.IntegerField()
    twopta = models.IntegerField()
    twoptm = models.IntegerField()


class Receiving(PlayerStat):
    rec = models.IntegerField()
    yds = models.IntegerField()
    tds = models.IntegerField()
    lng = models.IntegerField()
    lngtd = models.IntegerField()
    twopta = models.IntegerField()
    twoptm = models.IntegerField()


class Fumble(PlayerStat):
    tot = models.IntegerField()
    rcv = models.IntegerField()
    trcv = models.IntegerField()
    yds = models.IntegerField()
    lost = models.IntegerField()


class Kicking(PlayerStat):
    fgm = models.IntegerField()
    fga = models.IntegerField()
    fgyds = models.IntegerField()
    totpfg = models.IntegerField()
    xpmade = models.IntegerField()
    xpmissed = models.IntegerField()
    xpa = models.IntegerField()
    xpb = models.IntegerField()
    xptot = models.IntegerField()


class Punting(PlayerStat):
    pts = models.IntegerField()
    yds = models.IntegerField()
    avg = models.IntegerField()
    i20 = models.IntegerField()
    lng = models.IntegerField()


class KickRet(PlayerStat):
    ret = models.IntegerField()
    avg = models.IntegerField()
    tds = models.IntegerField()
    lng = models.IntegerField()
    lngtd = models.IntegerField()


class PuntRet(PlayerStat):
    ret = models.IntegerField()
    avg = models.IntegerField()
    tds = models.IntegerField()
    lng = models.IntegerField()
    lngtd = models.IntegerField()


class Defense(PlayerStat):
    tkl = models.IntegerField()
    ast = models.IntegerField()
    sk = models.IntegerField()
    int = models.IntegerField()
    ffum = models.IntegerField()