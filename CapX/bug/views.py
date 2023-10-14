from django.shortcuts import render, get_object_or_404
from .models import Bug

def register_bug(request):

def view_bug(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
