# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'wouldyourather.meta'
        db.add_column('ipmi_wouldyourather', 'meta',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'wouldyourather.meta'
        db.delete_column('ipmi_wouldyourather', 'meta')


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