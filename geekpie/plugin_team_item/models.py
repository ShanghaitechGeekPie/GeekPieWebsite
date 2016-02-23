from cms.models.pluginmodel import CMSPlugin

from django.db import models

class TeamItemModel(CMSPlugin):
    name = models.CharField(max_length=50, default='Name')
    describe = models.TextField(max_length=255, default='Describe')
