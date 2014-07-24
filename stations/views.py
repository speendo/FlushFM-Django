from django.http import HttpResponseRedirect
from stations.models import Station, Genre
from stations.forms import StationForm, GenreFormSet, AddressFormSet, GenreForm
from django.views.generic import CreateView, ListView


# List view
class StationList(ListView):
	model = Station
	context_object_name = 'stations'


# Create genre view
class GenreCreate(CreateView):
	model = Genre
	form_class = GenreForm


# Create station view
class StationCreate(CreateView):
	model = Station
	form_class = StationForm

	def get(self, request, *args, **kwargs):
		"""
		Handles GET requests and instantiates blank versions of the form
		and its inline formsets.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		genre_formset = GenreFormSet()
		address_formset = AddressFormSet()
		return self.render_to_response(
			self.get_context_data(form=form,
				genre_formset=genre_formset,
				address_formset=address_formset
			)
		)

	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance and its inline
		formsets with the passed POST variables and then checking them for
		validity.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		genre_formset = GenreFormSet(self.request.POST)
		address_formset = AddressFormSet(self.request.POST)
		if (form.is_valid() and genre_formset.is_valid() and
		address_formset.is_valid()):
			return self.form_valid(form, genre_formset, address_formset)
		else:
			return self.form_invalid(form, genre_formset, address_formset)

	def form_valid(self, form, genre_formset, address_formset):
		"""
		Called if all forms are valid. Creates a Recipe instance along with
		associated Ingredients and Instructions and then redirects to a
		success page.
		"""
		self.object = form.save()
		genre_formset.instance = self.object
		genre_formset.save()
		address_formset.instance = self.object
		address_formset.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, genre_formset, address_formset):
		"""
		Called if a form is invalid. Re-renders the context data with the
		data-filled forms and errors.
		"""
		return self.render_to_response(
			self.get_context_data(form=form,
				genre_formset=genre_formset,
				address_formset=address_formset
			)
		)
