from cms.models.pluginmodel import CMSPlugin

from django.db import models

class ActivityItemModel(CMSPlugin):
    name = models.CharField(max_length=50, default='Name')
    location = models.CharField(max_length=255, default='Location')
    datetime = models.DateTimeField()
    links = models.TextField(default='Links')
