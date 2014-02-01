from django.db import models

class Association(models.Model):
    '''
    Association information that exist in rockit network
    '''
    name = models.CharField(max_length=200, default='undefined')
    description = models.CharField(max_length=500, blank=True)
    namespace   = models.CharField(max_length=100)
    entry       = models.CharField(max_length=100)
    addable     = models.BooleanField(default=False)
    date_added  = models.DateTimeField(auto_now_add=True, blank=True)

class NodeCategory(models.Model):
    '''
    Node category in rockit network 
    '''
    name  = models.CharField(max_length=50, default='undefined')
    color = models.CharField(max_length=7, default='#000000')
    date_added    = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

class Node(models.Model):
    '''
    Describes a node in the rockit network. All devices should be coupled to a Node
    '''
    uuid = models.CharField(max_length=36,  blank=True)
    name = models.CharField(max_length=200, default='undefined')
    category       = models.ForeignKey(NodeCategory, null=True, blank=True, default=None)
    association    = models.ForeignKey(Association)
    aid            = models.CharField(max_length=100, blank=True)
    description    = models.CharField(max_length=500, blank=True)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)