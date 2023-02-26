from django.db import models

class Petplan(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)