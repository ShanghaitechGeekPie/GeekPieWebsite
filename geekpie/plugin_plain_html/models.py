from cms.models.pluginmodel import CMSPlugin

from django.db import models

class PlainHtml(CMSPlugin):
    body = models.TextField(blank=True)
