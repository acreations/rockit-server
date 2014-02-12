# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Node.type_generic'
        db.delete_column(u'razberry_node', 'type_generic')

        # Deleting field 'Node.type_basic'
        db.delete_column(u'razberry_node', 'type_basic')

        # Deleting field 'Node.type_specific'
        db.delete_column(u'razberry_node', 'type_specific')

        # Deleting field 'Node.frequent_listening'
        db.delete_column(u'razberry_node', 'frequent_listening')

        # Deleting field 'Node.type_security'
        db.delete_column(u'razberry_node', 'type_security')

        # Deleting field 'Node.device_name'
        db.delete_column(u'razberry_node', 'device_name')

        # Deleting field 'Node.max_baud_rate'
        db.delete_column(u'razberry_node', 'max_baud_rate')

        # Deleting field 'Node.security'
        db.delete_column(u'razberry_node', 'security')


    def backwards(self, orm):
        # Adding field 'Node.type_generic'
        db.add_column(u'razberry_node', 'type_generic',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Node.type_basic'
        db.add_column(u'razberry_node', 'type_basic',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Node.type_specific'
        db.add_column(u'razberry_node', 'type_specific',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Node.frequent_listening'
        db.add_column(u'razberry_node', 'frequent_listening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Node.type_security'
        db.add_column(u'razberry_node', 'type_security',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Node.device_name'
        db.add_column(u'razberry_node', 'device_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Node.max_baud_rate'
        db.add_column(u'razberry_node', 'max_baud_rate',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Node.security'
        db.add_column(u'razberry_node', 'security',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


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