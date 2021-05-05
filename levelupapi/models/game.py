from django.db import models

class Game(models.Model):
    
    name = models.CharField(max_length=55)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    difficulty = models.IntegerField()
    number_of_players = models.IntegerField()