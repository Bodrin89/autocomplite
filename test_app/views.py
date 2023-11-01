from dal import autocomplete
from django.shortcuts import render

# Create your views here.
from djangoProject.settings import LOGGER
from test_app.models import Address, District, City


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class DistrictAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return District.objects.none()

        city_id = self.forwarded.get('city', None)
        qs = District.objects.filter(city_id=city_id)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs