from django.db import models

class ActivityVOTModel(models.Model):
    name = models.CharField(max_length=255, default='Name')
    reply = models.TextField(default='Reply')
