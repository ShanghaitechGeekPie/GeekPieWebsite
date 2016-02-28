from cms.models.pluginmodel import CMSPlugin
from django.db import models

class MarkdownModel(CMSPlugin):
    content = models.TextField(default = '')
