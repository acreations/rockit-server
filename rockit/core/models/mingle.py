from django.db import models

class Hello(models.Model):
    """
    Keeps track of hellos
    """
    entry         = models.CharField(max_length=100, unique=True)
    done          = models.BooleanField(default=False)
    date_added    = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)