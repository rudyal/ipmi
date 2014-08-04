# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'wouldyourather.meta2'
        db.add_column('ipmi_wouldyourather', 'meta2',
                      self.gf('django.db.models.fields.CharField')(max_length=100, default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'wouldyourather.meta2'
        db.delete_column('ipmi_wouldyourather', 'meta2')


    models = {
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