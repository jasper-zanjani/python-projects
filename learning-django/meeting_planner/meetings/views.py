from django.shortcuts import render
from .models import Meeting

def detail(request, id):
  meeting = Meeting.objects.get(pk=id)
  return render(request, "meetings/detail.html", {"meeting": meeting})