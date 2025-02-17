from django.db import models


class FacetType(models.Model):
    organization = models.ForeignKey(
        "Organization", on_delete=models.PROTECT, blank=False, null=False
    )

    name = models.TextField(null=False, blank=False)

    # rules for assigning
    is_required = models.BooleanField()

    # rules for matching
    are_multiple_allowed = models.BooleanField()
    must_match_all = models.BooleanField()
    
    def __str__(self):
        return f"{self.pk}: {self.name}"