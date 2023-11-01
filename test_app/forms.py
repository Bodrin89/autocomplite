from dal import autocomplete

from django import forms

from test_app.models import Address, City, District

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

        widgets = {
            'city': autocomplete.ModelSelect2(url='country-autocomplete'),
            'district': autocomplete.ModelSelect2(url='district-autocomplete', forward=['city']),
        }

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['district'].widget.attrs['data-autocomplete-dependency'] = 'city'
