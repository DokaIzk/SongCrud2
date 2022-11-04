# from unittest.util import _MAX_LENGTH
from django.db import models
# from django.db import datetime


class Artiste(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Song(models.Model):
    title = models.CharField(max_length=40)
    released_date = models.DateTimeField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()
    artistes = models.ForeignKey('Artiste', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.CharField(max_length=2000)
    song_id = models.IntegerField()
    songs = models.OneToOneField('Song', on_delete=models.CASCADE)
