# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bookmark'
        db.create_table(u'bookmark_bookmark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookmark.Url'])),
            ('description', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookmark.Description'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookmark.Image'])),
        ))
        db.send_create_signal(u'bookmark', ['Bookmark'])

        # Adding M2M table for field tag on 'Bookmark'
        m2m_table_name = db.shorten_name(u'bookmark_bookmark_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bookmark', models.ForeignKey(orm[u'bookmark.bookmark'], null=False)),
            ('tag', models.ForeignKey(orm[u'bookmark.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bookmark_id', 'tag_id'])

        # Adding model 'Url'
        db.create_table(u'bookmark_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'bookmark', ['Url'])

        # Adding model 'Description'
        db.create_table(u'bookmark_description', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'bookmark', ['Description'])

        # Adding model 'Image'
        db.create_table(u'bookmark_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'bookmark', ['Image'])

        # Adding model 'Tag'
        db.create_table(u'bookmark_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'bookmark', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Bookmark'
        db.delete_table(u'bookmark_bookmark')

        # Removing M2M table for field tag on 'Bookmark'
        db.delete_table(db.shorten_name(u'bookmark_bookmark_tag'))

        # Deleting model 'Url'
        db.delete_table(u'bookmark_url')

        # Deleting model 'Description'
        db.delete_table(u'bookmark_description')

        # Deleting model 'Image'
        db.delete_table(u'bookmark_image')

        # Deleting model 'Tag'
        db.delete_table(u'bookmark_tag')


    models = {
        u'bookmark.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookmark.Description']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookmark.Image']"}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bookmark.Tag']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookmark.Url']"})
        },
        u'bookmark.description': {
            'Meta': {'object_name': 'Description'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bookmark.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'bookmark.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'bookmark.url': {
            'Meta': {'object_name': 'Url'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['bookmark']