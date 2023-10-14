from django.shortcuts import render
from django.http import HttpResponse

def your_view_function(request):
    # Your view logic here
    return HttpResponse("This is your view.")
