from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .forms import PlaceForm
from .models import Place


# Create your views here.
def newplace(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("TNX")

    else:
        form = PlaceForm()

    return render(request, 'newplace.html', {'form': form})


class PlaceDetailView(DetailView):
    model = Place


def place_detail_view_func(request, id):
    place_instance = Place.objects.get(id=id)
    template = "places/places_detail.html"
    context = {
        "object": place_instance,
    }
    return render(request, template, context)
