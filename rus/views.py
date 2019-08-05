from django.shortcuts import render
from django.http import HttpResponse
from .models import Rate

def index(request):
    output = ''.join(["<p>%s - %f</p>"%(rate.currency, rate.rate) for rate in Rate.objects.all()])
    return HttpResponse(output)