from django.db import models


class Organization(models.Model):
    identifier = models.TextField(unique=True)
    name = models.TextField(blank=True, null=True)
 