from django.db import models

class Node(models.Model):
    '''
    Describes a RaZberry Z-Wave node
    '''
    device_id = models.CharField(max_length=100)

    device_type = models.CharField(max_length = 50, default = '')

    manufacturer_id   = models.CharField(max_length = 50, default = '')
    manufacturer_name = models.CharField(max_length = 50, default = '')
    
    version  = models.PositiveSmallIntegerField(default = 0)

    listening = models.BooleanField(default = False)
    routing  = models.BooleanField(default = False)
    beaming  = models.BooleanField(default = False)
    awaken   = models.BooleanField(default = False)
    failed   = models.BooleanField(default = False)

    date_added    = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

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