from django.db import models

class SchoolModel(models.Model):
    name = models.CharField(max_length=200)
    coordinates = models.JSONField()
