from django.db import models

class Alarm(models.Model):
    """
    Defines a time to tigger events/actions
    """
    cron   = models.CharField(max_length=50, blank=True)
    repeat = models.BooleanField(default=False)
    date_next      = models.DateTimeField(blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)