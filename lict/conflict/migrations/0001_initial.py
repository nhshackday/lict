# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('conflict_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pmc', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pmid', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('raw_conflict_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('conflict', ['Article'])

        # Adding model 'Organisation'
        db.create_table('conflict_organisation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('conflict', ['Organisation'])

        # Adding model 'Conflict'
        db.create_table('conflict_conflict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['conflict.Article'])),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['conflict.Organisation'])),
        ))
        db.send_create_signal('conflict', ['Conflict'])

        # Adding model 'Drug'
        db.create_table('conflict_drug', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jeff_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('conflict', ['Drug'])

        # Adding model 'ArticleDrugs'
        db.create_table('conflict_articledrugs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['conflict.Article'])),
            ('drug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['conflict.Drug'])),
        ))
        db.send_create_signal('conflict', ['ArticleDrugs'])

        # Adding model 'Mesh'
        db.create_table('conflict_mesh', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jeff_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('conflict', ['Mesh'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('conflict_article')

        # Deleting model 'Organisation'
        db.delete_table('conflict_organisation')

        # Deleting model 'Conflict'
        db.delete_table('conflict_conflict')

        # Deleting model 'Drug'
        db.delete_table('conflict_drug')

        # Deleting model 'ArticleDrugs'
        db.delete_table('conflict_articledrugs')

        # Deleting model 'Mesh'
        db.delete_table('conflict_mesh')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['conflict']