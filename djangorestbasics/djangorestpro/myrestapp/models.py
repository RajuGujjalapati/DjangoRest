from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=60)
# Create your models here.
