from django.forms import ModelForm
from django.forms.widgets import TextInput
from django.forms.models import inlineformset_factory

from stations.models import Station, StationGenre, Address, Genre

class StationForm(ModelForm):
    class Meta:
        model = Station

GenreFormSet = inlineformset_factory(Station, StationGenre)
AddressFormSet = inlineformset_factory(Station, Address)

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        widgets = {
                   'color': TextInput(attrs={'type': 'color'}),
                   }