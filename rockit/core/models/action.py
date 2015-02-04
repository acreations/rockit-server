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

class ActionFinish(models.Model):
    """
    Holder for finish action
    """
    holder  = models.ForeignKey(Action)
    target  = models.ForeignKey(Association)
    identifier = models.CharField(max_length = 50)

class ActionThen(models.Model):
    """
    Holder for then action
    """
    holder  = models.ForeignKey(Action)
    target  = models.ForeignKey(Association)
    identifier = models.CharField(max_length = 50)

class ActionWhen(models.Model):
    """
    Holder for when action is triggered
    """
    holder  = models.ForeignKey(Action)
    target  = models.ForeignKey(Association)
    identifier = models.CharField(max_length = 50)