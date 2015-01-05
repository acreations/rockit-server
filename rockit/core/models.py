from django.db import models

class Association(models.Model):
    """
    Plugin information that exist in Rockit network
    """
    name = models.CharField(max_length=200, default='undefined')
    description  = models.CharField(max_length=500, blank=True)
    namespace    = models.CharField(max_length=100)
    entry        = models.CharField(max_length=100)
    addable      = models.BooleanField(default=False)
    when_addable = models.BooleanField(default=False)
    then_addable = models.BooleanField(default=False)
    date_added   = models.DateTimeField(auto_now_add=True, blank=True)

class Action(models.Model):
    """
    Action that used to call a function in rockit network
    """
    name = models.CharField(max_length=200, default='undefined')
    description = models.CharField(max_length=500, blank=True)
    association = models.ForeignKey(Association)
    aid         = models.CharField(max_length=100, blank=True)
    params      = models.CharField(max_length=1000, blank=True)
    favorite    = models.BooleanField(default=False)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)

class Schedule(models.Model):
    """
    Defines a time to tigger events/actions
    """
    cron = models.CharField(max_length=50, blank=True)
    done = models.BooleanField(default=False)
    date_next      = models.DateTimeField(blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)

class NodeCategory(models.Model):
    """
    Node category in rockit network
    """
    name  = models.CharField(max_length=50, default='undefined')
    color = models.CharField(max_length=7, default='#000000')
    date_added    = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

class Node(models.Model):
    """
    Describes a node in the rockit network.
    """
    uuid = models.CharField(max_length=36,  blank=True, unique=True)
    name = models.CharField(max_length=200, default='undefined')
    category       = models.ForeignKey(NodeCategory, null=True, blank=True, default=None)
    association    = models.ForeignKey(Association)
    aid            = models.CharField(max_length=100, blank=True)
    description    = models.CharField(max_length=500, blank=True)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)

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

class UserRole(models.Model):
    """
    Create a role based user model
    """
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)

class User(models.Model):
    """
    Defines a user that can be used with rockit server
    """
    openid = models.CharField(max_length=36, blank=True)
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)