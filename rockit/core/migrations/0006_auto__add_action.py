# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table(u'core_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='undefined', max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('association', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Association'])),
            ('aid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('params', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('favorite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Action'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table(u'core_action')


    models = {
        u'core.action': {
            'Meta': {'object_name': 'Action'},
            'aid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'association': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Association']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '200'}),
            'params': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        },
        u'core.association': {
            'Meta': {'object_name': 'Association'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'entry': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '200'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'then_addable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'when_addable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.node': {
            'Meta': {'object_name': 'Node'},
            'aid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'association': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Association']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.NodeCategory']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.nodecategory': {
            'Meta': {'object_name': 'NodeCategory'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#000000'", 'max_length': '7'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '50'})
        }
    }

    complete_apps = ['core']