from django.db import models

class Node(models.Model):
    '''
    Describes a RaZberry Z-Wave node
    '''
    node_id = models.CharField(max_length=100)

    product_name = models.CharField(max_length = 50, default = '')
    product_type = models.CharField(max_length = 50, default = '')
    product_id   = models.CharField(max_length = 50, default = '')

    manufacturer_id   = models.CharField(max_length = 50, default = '')
    manufacturer_name = models.CharField(max_length = 50, default = '')
    
    type_generic  = models.PositiveSmallIntegerField(default = 0)
    type_basic    = models.PositiveSmallIntegerField(default = 0)
    type_specific = models.PositiveSmallIntegerField(default = 0)
    type_security = models.PositiveSmallIntegerField(default = 0)
    
    version  = models.PositiveSmallIntegerField(default = 0)

    listening = models.BooleanField(default = False)
    frequent_listening = models.BooleanField(default = False)
    routing  = models.BooleanField(default = False)
    beaming  = models.BooleanField(default = False)
    security = models.BooleanField(default = False)
    sleeping = models.BooleanField(default = False)
    locked   = models.BooleanField(default = False)
    
    max_baud_rate = models.PositiveSmallIntegerField(default = 0)

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