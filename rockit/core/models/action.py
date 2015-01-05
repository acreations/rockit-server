from django.db import models

from rockit.core.models import Association
from rockit.core.models import Node

class Action(models.Model):
    """
    Action that used to call a function in rockit network
    """
    name = models.CharField(max_length=200, default='undefined')
    description    = models.CharField(max_length=500, blank=True)
    favorite       = models.BooleanField(default=False)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)

class ActionThen(models.Model):
    """
    Action that take care of specific task (setter)
    """
    target  = models.ForeignKey(Node)
    command = models.CharField(max_length=200)
    value   = models.CharField(max_length=100)

class Schedule(models.Model):
    """
    Defines a time to tigger events/actions
    """
    cron = models.CharField(max_length=50, blank=True)
    done = models.BooleanField(default=False)
    date_next      = models.DateTimeField(blank=True)
    date_modified  = models.DateTimeField(auto_now=True, blank=True)
    date_added     = models.DateTimeField(auto_now_add=True, blank=True)