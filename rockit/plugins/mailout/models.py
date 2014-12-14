from django.db import models

class Server(models.Model):
    """
    Server configuration for mail
    """
    name = models.CharField(max_length=200, default='undefined')
    description  = models.CharField(max_length=500, blank=True)
    date_added    = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

class Node(models.Model):
    """
    Mailout Node
    """
    server = models.ForeignKey(Server)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)

class Setting(models.Model):
    """
    Settings
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    value       = models.CharField(max_length=100, blank=True)
    readonly    = models.BooleanField(default=True)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)