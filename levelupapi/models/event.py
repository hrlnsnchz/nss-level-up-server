from django.db import models

class Event(models.Model):

    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    guest = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    datetime = models.DateTimeField()