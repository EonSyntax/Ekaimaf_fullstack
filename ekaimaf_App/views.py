from django.shortcuts import render
from . import views

# Create your views here.
def coming_soon(request): 
    return render(request, 'pages/coming_soon.html')