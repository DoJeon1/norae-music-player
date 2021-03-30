from django.db import models

# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=200)
    song_duration = models.IntegerField(default=0)

    def __str__(self):
        return self.song_title
