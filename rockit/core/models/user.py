from django.db import models

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