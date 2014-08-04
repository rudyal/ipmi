# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ipmi'
        db.create_table('ipmi_ipmi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serv_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('power', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cpu_temp', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cpu_temp2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fan_speed', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('air', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('knox', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('meta1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('meta2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('meta3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('meta4', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('meta5', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('ipmi', ['ipmi'])


    def backwards(self, orm):
        # Deleting model 'ipmi'
        db.delete_table('ipmi_ipmi')


    models = {
        'ipmi.ipmi': {
            'Meta': {'object_name': 'ipmi'},
            'air': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cpu_temp': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cpu_temp2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'fan_speed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'knox': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'meta1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'meta2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'meta3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'meta4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'meta5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'power': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serv_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ipmi.wouldyourather': {
            'Meta': {'object_name': 'wouldyourather'},
            'answer1': ('django.db.models.fields.BooleanField', [], {}),
            'answer2': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'meta2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ipmi']