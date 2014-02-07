from rockit.foundation.core import models
from rockit.foundation.core import serializers

class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows node categories to be view and set
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer