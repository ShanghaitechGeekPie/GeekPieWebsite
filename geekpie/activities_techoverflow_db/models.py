from django.db import models

class ActivityTechOverflowModel(models.Model):
    name = models.CharField(max_length=255, default='Name')
    phone = models.CharField(max_length=255, default='Phone')
    email = models.CharField(max_length=255, default='Email')
    target = models.IntegerField(default=1)
