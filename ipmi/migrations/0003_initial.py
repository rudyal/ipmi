# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'wouldyourather'
        db.create_table('ipmi_wouldyourather', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('meta', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('answer1', self.gf('django.db.models.fields.BooleanField')()),
            ('answer2', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('ipmi', ['wouldyourather'])


    def backwards(self, orm):
        # Deleting model 'wouldyourather'
        db.delete_table('ipmi_wouldyourather')


    models = {
        'ipmi.wouldyourather': {
            'Meta': {'object_name': 'wouldyourather'},
            'answer1': ('django.db.models.fields.BooleanField', [], {}),
            'answer2': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ipmi']