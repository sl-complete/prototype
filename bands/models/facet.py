from django.db import models


class Facet(models.Model):
    type = models.ForeignKey(
        "FacetType", on_delete=models.PROTECT, blank=False, null=False
    )
    
    value = models.TextField()

    def __str__(self):
        return f"{self.pk}: {self.value}"    