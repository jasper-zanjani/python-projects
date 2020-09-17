from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

def welcome(request):
  return render(request,"website/welcome.html", {"meetings": Meeting.objects.all()})

def date(req):
  return HttpResponse(f'This page was served at {datetime.now()}')

def about(req):
  return HttpResponse(f'I\'m an impatient but dilligent, hard-working, overweight programmer.')