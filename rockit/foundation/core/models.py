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