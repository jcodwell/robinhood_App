from django.db import models

# Create your models here.

""" Model for Crypto About Info"""
class AboutInfo_Crypto(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    tradability = models.CharField(max_length=200)    
