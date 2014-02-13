from rest_framework import serializers

from rockit.plugins.mailout import models

class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = models.Node
        read_only_fields = ('date_added', 'date_modified')

class ServerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = models.Server
        read_only_fields = ('date_added', 'date_modified')