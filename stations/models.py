from django.db import models
from django.core.urlresolvers import reverse


class Genre(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(max_length=140, null=True)
	color = models.CharField(max_length=6, null=True)
	copyOf = models.ForeignKey("self", null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('stations:list')


class Station(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField(max_length=140)
	# Genre (Many-To-Many)
#	genre = models.ManyToManyField(Genre)
	genres = models.ManyToManyField(Genre, through='StationGenre')
	created_at = models.DateTimeField(auto_now_add=False, null=True)
	last_modified_at = models.DateTimeField(auto_now=False, null=True)
	last_listened_at = models.DateTimeField(null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('stations:list')


class Address(models.Model):
	url = models.URLField()
	priority = models.PositiveSmallIntegerField()
	is_working = models.BooleanField(default=True)
	# Station (Many-To-One)
	station = models.ForeignKey(Station)

	def __str__(self):
		return self.url


class StationGenre(models.Model):
	station = models.ForeignKey(Station)
	genre = models.ForeignKey(Genre)

	def __str__(self):
		return self.url