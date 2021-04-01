from django.db import models

# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=200)
    song_artist = models.CharField(max_length=200)
    song_duration = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='media')
    song_file = models.FileField(upload_to='media')

    def __str__(self):
        return self.song_title
