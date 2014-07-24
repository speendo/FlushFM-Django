from django.forms import ModelForm
from django.forms.widgets import TextInput, URLInput
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, ButtonHolder, Submit
from django.core.urlresolvers import reverse

from stations.models import Station, StationGenre, Address, Genre


class GenreForm(ModelForm):
	class Meta:
		model = Genre
		widgets = {
			'color': TextInput(attrs={'class': 'color-picker'}),
			}

	def __init__(self, *args, **kwargs):
		super(GenreForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_action = '.'
		self.helper.redirect_url = reverse('stations:list')

		self.helper.layout = Layout(
			Field('name'),
			Field('description'),
			Field('color'),
			ButtonHolder(
				Button('cancel', 'Cancel'),
				Submit('submit', 'Create'),
				css_class='pull-right'
			)
		)
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-2 col-xs-3'
		self.helper.field_class = 'col-md-10 col-xs-9'


class StationForm(ModelForm):
	class Meta:
		model = Station

	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()

		self.helper.layout = Layout(
			Field('name'),
			Field('description'),
			ButtonHolder(
				Submit('submit', 'Create'),
				Button('cancel', 'Cancel')
			)
		)
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-2 col-xs-3'
		self.helper.field_class = 'col-md-10 col-xs-9'

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
