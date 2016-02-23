from cms.models.pluginmodel import CMSPlugin

from django.db import models

class ProjectItemModel(CMSPlugin):
    name = models.CharField(max_length=50, default='Name')
    logo = models.CharField(max_length=255, default='Logo')
    url = models.CharField(max_length=255, default='URL')
    color = models.CharField(max_length=255, default='Color')
