from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Meme(models.Model):
    category = models.CharField()
    pic_text = models.CharField()
    # date_added = models.CharField()
    rank = models.IntegerField()
    views = models.IntegerField()
    link = models.CharField()