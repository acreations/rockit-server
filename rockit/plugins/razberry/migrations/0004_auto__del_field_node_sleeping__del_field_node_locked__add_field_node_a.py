# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Node.sleeping'
        db.delete_column(u'razberry_node', 'sleeping')

        # Deleting field 'Node.locked'
        db.delete_column(u'razberry_node', 'locked')

        # Adding field 'Node.awaken'
        db.add_column(u'razberry_node', 'awaken',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Node.failed'
        db.add_column(u'razberry_node', 'failed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Node.sleeping'
        db.add_column(u'razberry_node', 'sleeping',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Node.locked'
        db.add_column(u'razberry_node', 'locked',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Node.awaken'
        db.delete_column(u'razberry_node', 'awaken')

        # Deleting field 'Node.failed'
        db.delete_column(u'razberry_node', 'failed')


    models = {
        u'razberry.node': {
            'Meta': {'object_name': 'Node'},
            'awaken': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'beaming': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'device_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'device_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frequent_listening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manufacturer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'manufacturer_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'max_baud_rate': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'routing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'security': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type_basic': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'type_generic': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'type_security': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'type_specific': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'version': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
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