from django.db import models

class Node(models.Model):
    '''
    Describes a RaZberry Z-Wave node
    '''
    device_id = models.CharField(max_length=100)

    device_type = models.CharField(max_length = 50, default = '')

    manufacturer_id   = models.CharField(max_length = 50, default = '')
    manufacturer_name = models.CharField(max_length = 50, default = '')
    
    version = models.CharField(max_length = 10, default = '')

    listening = models.BooleanField(default = False)
    routing  = models.BooleanField(default = False)
    beaming  = models.BooleanField(default = False)
    awaken   = models.BooleanField(default = False)
    failed   = models.BooleanField(default = False)

    date_added    = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class NodeVersion(models.Model):
    """
    Node libraries version
    """
    node = models.ForeignKey(Node)
    sdk  = models.CharField(max_length = 16, default = '')

    application = models.CharField(max_length = 16, default = '')
    zw_library  = models.IntegerField(default=0)
    zw_protocol = models.CharField(max_length = 16, default = '')

class Setting(models.Model):
    """
    Settings in rockit network
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    value       = models.CharField(max_length=100, blank=True)
    readonly    = models.BooleanField(default=True)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)