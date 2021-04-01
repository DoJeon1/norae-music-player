from django.db import models

# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=200)
    song_artist = models.CharField(max_length=200, default='')
    song_duration = models.DurationField(default='')
    song_file = models.FileField(upload_to='media', default=False)
    cover_image = models.ImageField(upload_to='media', default=False)

    def __str__(self):
        return self.song_title
