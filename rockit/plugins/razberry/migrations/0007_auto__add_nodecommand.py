# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NodeCommand'
        db.create_table(u'razberry_nodecommand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['razberry.Node'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('identifier', self.gf('django.db.models.fields.IntegerField')()),
            ('namespace', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'razberry', ['NodeCommand'])


    def backwards(self, orm):
        # Deleting model 'NodeCommand'
        db.delete_table(u'razberry_nodecommand')


    models = {
        u'razberry.node': {
            'Meta': {'object_name': 'Node'},
            'awaken': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'beaming': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'device_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manufacturer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'manufacturer_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'routing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        u'razberry.nodecommand': {
            'Meta': {'object_name': 'NodeCommand'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'namespace': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['razberry.Node']"})
        },
        u'razberry.nodeversion': {
            'Meta': {'object_name': 'NodeVersion'},
            'application': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['razberry.Node']"}),
            'sdk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            'zw_library': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'zw_protocol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'})
        },
        u'razberry.setting': {
            'Meta': {'object_name': 'Setting'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'readonly': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['razberry']