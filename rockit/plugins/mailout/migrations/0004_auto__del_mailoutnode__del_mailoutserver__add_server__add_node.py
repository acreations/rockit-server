# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'MailoutNode'
        db.delete_table(u'mailout_mailoutnode')

        # Deleting model 'MailoutServer'
        db.delete_table(u'mailout_mailoutserver')

        # Adding model 'Server'
        db.create_table(u'mailout_server', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='undefined', max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mailout', ['Server'])

        # Adding model 'Node'
        db.create_table(u'mailout_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailout.Server'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mailout', ['Node'])


    def backwards(self, orm):
        # Adding model 'MailoutNode'
        db.create_table(u'mailout_mailoutnode', (
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailout.MailoutServer'])),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mailout', ['MailoutNode'])

        # Adding model 'MailoutServer'
        db.create_table(u'mailout_mailoutserver', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='undefined', max_length=200)),
        ))
        db.send_create_signal(u'mailout', ['MailoutServer'])

        # Deleting model 'Server'
        db.delete_table(u'mailout_server')

        # Deleting model 'Node'
        db.delete_table(u'mailout_node')


    models = {
        u'mailout.node': {
            'Meta': {'object_name': 'Node'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailout.Server']"})
        },
        u'mailout.server': {
            'Meta': {'object_name': 'Server'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '200'})
        }
    }

    complete_apps = ['mailout']