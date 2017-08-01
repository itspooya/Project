from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import PlaceForm
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