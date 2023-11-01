from django.contrib import admin

# Register your models here.
from test_app.forms import  AddressForm
from test_app.models import City, District, Address


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    form = AddressForm

