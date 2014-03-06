from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from stations.models import Station, Genre, Address

class StationForm(ModelForm):
    class Meta:
        model = Station

#GenreFormSet = inlineformset_factory(Station, Genre)
AddressFormSet = inlineformset_factory(Station, Address)