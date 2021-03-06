from django.db import models

class Setting(models.Model):
    """
    Settings
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    value       = models.CharField(max_length=100, blank=True)
    readonly    = models.BooleanField(default=False)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)