# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Organisation.is_a_real_organisation'
        db.add_column('conflict_organisation', 'is_a_real_organisation',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Organisation.is_a_real_organisation'
        db.delete_column('conflict_organisation', 'is_a_real_organisation')


    models = {
        'conflict.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pmc': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pmid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'raw_conflict_text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'conflict.articledrugs': {
            'Meta': {'object_name': 'ArticleDrugs'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conflict.Article']"}),
            'drug': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conflict.Drug']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'conflict.conflict': {
            'Meta': {'object_name': 'Conflict'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conflict.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conflict.Organisation']"})
        },
        'conflict.drug': {
            'Meta': {'object_name': 'Drug'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jeff_id': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'conflict.mesh': {
            'Meta': {'object_name': 'Mesh'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jeff_id': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'conflict.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_a_real_organisation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['conflict']