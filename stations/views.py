from django.http import HttpResponseRedirect
from django.shortcuts import render
from stations.models import Station
from stations.forms import StationForm, GenreFormSet, AddressFormSet

# List view
from django.views.generic import ListView
class StationList(ListView):
    model = Station
    context_object_name = 'stations'
    
# Create view
from django.views.generic import CreateView
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
        genre_form = GenreFormSet()
        address_form = AddressFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  genre_form=genre_form,
                                  address_form=address_form))
        
def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        genre_form = GenreFormSet(self.request.POST)
        address_form = AddressFormSet(self.request.POST)
        if (form.is_valid() and genre_form.is_valid() and address_form.is_valid()):
            return self.form_valid(form, genre_form, address_form)
            return self.form_valid(form, address_form)
        else:
            return self.form_invalid(form, genre_form, address_form)
            return self.form_invalid(form, address_form)

def form_valid(self, form, genre_form, address_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        genre_form.instance = self.object
        genre_form.save()
        address_form.instance = self.object
        address_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
def form_invalid(self, form, genre_form, address_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  genre_form=genre_form,
                                  address_form=address_form))