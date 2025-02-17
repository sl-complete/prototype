from django.db import models


class Employee(models.Model):
    organization = models.ForeignKey("Organization", on_delete=models.PROTECT)
    facets = models.ManyToManyField("Facet")

    name = models.TextField()

    def __str__(self):
        return f"{self.pk}: {self.name}"