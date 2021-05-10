from django.db import models

class Event(models.Model):

    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default="")
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateField(default="2021-08-14")
    time = models.TimeField(default="12:00")