from rest_framework import serializers

from rockit.foundation.core import models

class AssociationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = models.Association
        read_only_fields = ('date_added',)

class NodeCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.NodeCategory
        read_only_fields = ('date_added', 'date_modified')

class NodeSerializer(serializers.HyperlinkedModelSerializer):

    category = serializers.RelatedField(many=False)
    association = AssociationSerializer(many=False)

    class Meta:
        model  = models.Node
        read_only_fields = ('date_added', 'date_modified')
        fields = ('url', 'aid', 'category', 'association')