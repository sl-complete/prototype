from django.db import models


class Band(models.Model):
    class BandType(models.TextChoices):
        salary = "salary", "Salary"
        equity = "equity", "Equity"

    organization = models.ForeignKey(
        "Organization", on_delete=models.PROTECT, blank=False, null=False
    )

    facets = models.ManyToManyField("Facet")

    band_type = models.TextField(null=False, blank=False, choices=BandType.choices)
    min = models.BigIntegerField(blank=False, null=False)
    target = models.BigIntegerField(blank=False, null=False)
    max = models.BigIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.pk}: {self.min} - {self.target} - {self.max}"