from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def coming_soon(request): 
    return render(request, 'pages/coming_soon.html')


def healthz(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        # database is up
        return HttpResponse("OK", status=200)
    except Exception:
        return HttpResponse("DB Error", status=500)