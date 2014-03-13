# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Genre.color'
        db.add_column('stations_genre', 'color',
                      self.gf('django.db.models.fields.CharField')(max_length=7, null=True),
                      keep_default=False)

        # Adding field 'Station.created_at'
        db.add_column('stations_station', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'Station.last_modified_at'
        db.add_column('stations_station', 'last_modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'Station.last_listened_at'
        db.add_column('stations_station', 'last_listened_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Genre.color'
        db.delete_column('stations_genre', 'color')

        # Deleting field 'Station.created_at'
        db.delete_column('stations_station', 'created_at')

        # Deleting field 'Station.last_modified_at'
        db.delete_column('stations_station', 'last_modified_at')

        # Deleting field 'Station.last_listened_at'
        db.delete_column('stations_station', 'last_listened_at')


    models = {
        'stations.address': {
            'Meta': {'object_name': 'Address'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_working': ('django.db.models.fields.BooleanField', [], {}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Station']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'stations.genre': {
            'Meta': {'object_name': 'Genre'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'stations.station': {
            'Meta': {'object_name': 'Station'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['stations.StationGenre']", 'symmetrical': 'False', 'to': "orm['stations.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_listened_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_modified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'stations.stationgenre': {
            'Meta': {'object_name': 'StationGenre'},
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Station']"})
        }
    }

    complete_apps = ['stations']