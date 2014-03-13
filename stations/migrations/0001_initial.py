# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table('stations_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('stations', ['Genre'])

        # Adding model 'Station'
        db.create_table('stations_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('stations', ['Station'])

        # Adding model 'Address'
        db.create_table('stations_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('is_working', self.gf('django.db.models.fields.BooleanField')()),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stations.Station'])),
        ))
        db.send_create_signal('stations', ['Address'])

        # Adding model 'StationGenre'
        db.create_table('stations_stationgenre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stations.Station'])),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stations.Genre'])),
        ))
        db.send_create_signal('stations', ['StationGenre'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table('stations_genre')

        # Deleting model 'Station'
        db.delete_table('stations_station')

        # Deleting model 'Address'
        db.delete_table('stations_address')

        # Deleting model 'StationGenre'
        db.delete_table('stations_stationgenre')


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
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'stations.station': {
            'Meta': {'object_name': 'Station'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stations.Genre']", 'symmetrical': 'False', 'through': "orm['stations.StationGenre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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