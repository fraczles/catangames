from django.db import models
from django.conf import settings

from .managers import GameManager


class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='game')
    winner = models.ForeignKey('players.User', null=True, on_delete=models.SET_NULL)
    players = models.ManyToManyField('players.User', related_name='players')

    objects = GameManager()

    class Meta:
        verbose_name = "game"
        verbose_name_plural = "games"

    def __repr__(self):
        return str(self.date)

    def __str__(self):
        return str(self.date)

