from django.db import models
    
class Genre(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    
class Station(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    # Genre (Many-To-Many)
#    genre = models.ManyToManyField(Genre)
    genres = models.ManyToManyField(Genre, through='StationGenre')

class Address(models.Model):
    url = models.URLField()
    priority = models.PositiveSmallIntegerField()
    is_working = models.BooleanField()
    # Station (Many-To-One)
    station = models.ForeignKey(Station)
    
class StationGenre(models.Model):
    station = models.ForeignKey(Station)
    genre = models.ForeignKey(Genre)