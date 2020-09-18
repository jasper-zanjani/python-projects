from django.shortcuts import render
from starships.models import Starship
# Create your views here.

def home(request):
  return render(request, 'website/home.html', {'ships': Starship.objects.all()})
