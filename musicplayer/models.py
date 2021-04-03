from django.db import models

# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=200)
    song_artist = models.CharField(max_length=200, default='')
    song_duration = models.DurationField(default='')
    song_file = models.FileField()
    cover_image = models.ImageField()
    paginate_by = 2

    def __str__(self):
        return self.song_title
