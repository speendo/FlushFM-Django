from django.db import models
    
class Genre(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    color = models.CharField(max_length=7, null=True)
    
class Station(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    # Genre (Many-To-Many)
#    genre = models.ManyToManyField(Genre)
    genres = models.ManyToManyField(Genre, through='StationGenre')
    created_at = models.DateTimeField(auto_now_add=False, null=True)
    last_modified_at = models.DateTimeField(auto_now=False, null=True)
    last_listened_at = models.DateTimeField(null=True)

class Address(models.Model):
    url = models.URLField()
    priority = models.PositiveSmallIntegerField()
    is_working = models.BooleanField()
    # Station (Many-To-One)
    station = models.ForeignKey(Station)
    
class StationGenre(models.Model):
    station = models.ForeignKey(Station)
    genre = models.ForeignKey(Genre)