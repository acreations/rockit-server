# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table(u'razberry_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('product_type', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('product_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('manufacturer_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('manufacturer_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('type_generic', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('type_basic', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('type_specific', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('type_security', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('version', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('listening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('frequent_listening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('routing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('beaming', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('security', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sleeping', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('locked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_baud_rate', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'razberry', ['Node'])


    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table(u'razberry_node')


    models = {
        u'razberry.node': {
            'Meta': {'object_name': 'Node'},
            'beaming': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'frequent_listening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manufacturer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'manufacturer_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'max_baud_rate': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'node_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'product_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'product_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'routing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'security': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sleeping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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