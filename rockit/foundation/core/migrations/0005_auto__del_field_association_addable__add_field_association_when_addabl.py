# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Association.addable'
        db.delete_column(u'core_association', 'addable')

        # Adding field 'Association.when_addable'
        db.add_column(u'core_association', 'when_addable',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Association.then_addable'
        db.add_column(u'core_association', 'then_addable',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Association.addable'
        db.add_column(u'core_association', 'addable',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Association.when_addable'
        db.delete_column(u'core_association', 'when_addable')

        # Deleting field 'Association.then_addable'
        db.delete_column(u'core_association', 'then_addable')


    models = {
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