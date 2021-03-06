from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird
from .forms import SightingForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds' : birds })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    sighting_form = SightingForm()
    return render(request, 'birds/detail.html', { 'bird' : bird, 'sighting_form': sighting_form })

def add_sighting(request, bird_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.bird_id = bird_id
        new_sighting.save()
    return redirect('detail', bird_id=bird_id)


class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ('family', 'habitat', 'food', 'nesting', 'behavior', 'description')

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'