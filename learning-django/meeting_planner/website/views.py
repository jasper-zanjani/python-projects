from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
  return HttpResponse("Welcome to the Meeting Planner!")

def date(req):
  return HttpResponse(f'This page was served at {datetime.now()}')

def about(req):
  return HttpResponse(f'I\'m an impatient but dilligent, hard-working, overweight programmer.')