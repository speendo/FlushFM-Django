from django.contrib import admin
from stations.models import Genre, Station, Address, StationGenre


class AddressInline(admin.TabularInline):
	model = Address


class StationGenreInline(admin.TabularInline):
	model = StationGenre


class GenreInline(admin.ModelAdmin):
	inlines = [
		StationGenreInline,
	]


class StationAdmin(admin.ModelAdmin):
	inlines = [
		AddressInline,
		StationGenreInline,
	]


admin.site.register(Station, StationAdmin)
admin.site.register(Genre,)
