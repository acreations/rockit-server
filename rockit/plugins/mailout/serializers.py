from rest_framework import serializers

from rockit.plugins.mailout import models

class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = models.Node
        read_only_fields = ('date_added', 'date_modified')
        fields = ('url', 'server')