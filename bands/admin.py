from django.contrib import admin
from django.db.models import Q, Count, F, Exists, OuterRef, Subquery
from django.db.models.functions import Coalesce

from bands.models import Band, Employee, Facet, FacetType, Organization


class CommonAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    def match_employee_to_band(self, request, queryset):
        organization = Organization.objects.get(pk=1)

        # Get all facet types for the organization
        facet_types = FacetType.objects.filter(
            organization=organization
        )
        
        # Start with basic band filter for the organization
        base_query = Band.objects.filter(
            organization=organization
        )
                
        employee = Employee.objects.get(pk=1)
        print(employee.facets.all())

        # Build complex Q object for facet matching
        facet_conditions = Q()
        
        for facet_type in facet_types:
            # Get employee's facets of this type
            employee_facets = employee.facets.filter(
                type=facet_type
            )
            
            # Create subquery to check band's facets
            band_facets_subquery = Band.facets.through.objects.filter(
                band=OuterRef('pk'),
                facet__type=facet_type
            )
            
            if facet_type.must_match_all:
                # Band must have all facets employee has of this type
                for facet in employee_facets:
                    facet_conditions &= Exists(
                        band_facets_subquery.filter(facet=facet)
                    )
            else:
                # Band must have at least one matching facet of this type
                facet_conditions &= Exists(
                    band_facets_subquery.filter(
                        facet__in=employee_facets
                    )
                )
        
        # Apply all facet conditions to base query
        matching_bands = base_query.filter(facet_conditions)
        print(matching_bands)
        if matching_bands:
            print(matching_bands[0].facets.all())

    actions = ['match_employee_to_band']


admin.site.register(Band, CommonAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Facet, CommonAdmin)
admin.site.register(FacetType, CommonAdmin)