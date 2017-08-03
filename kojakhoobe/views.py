from django.shortcuts import render
from django.views.generic.detail import DetailView

from Places.models import Place


# Create your views here.
class PlaceDetailView(DetailView):
    model = Place


def place_detail_view_func(request, id):
    place_instance = Place.objects.get(id=id)
    template = "places/places_detail.html"
    context = {
        "object": place_instance
    }
    return render(request, template, context)
