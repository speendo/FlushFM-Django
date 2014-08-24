from django.forms import ModelForm
from django.forms.widgets import TextInput, URLInput
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse

from stations.models import Station, StationGenre, Address, Genre


class GenreForm(ModelForm):
	class Meta:
		model = Genre
		widgets = {
			'color': TextInput(attrs={'class': 'color-picker'}),
			}


class StationForm(ModelForm):
	class Meta:
		model = Station

GenreFormSet = inlineformset_factory(Station, StationGenre)

AddressFormSet = inlineformset_factory(
	Station,
	Address,
	can_order=True,
	extra=1,
	widgets={
		'url': URLInput(attrs={
			'class': 'address_url',
			'data-clear-btn': 'true'
		}),
	}
)
