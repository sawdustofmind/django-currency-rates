from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from .models import Rate

import requests
from bs4 import BeautifulSoup

def index(request):
    output = ''.join(["<p>%s - %f</p>"%(rate.currency, rate.rate) for rate in Rate.objects.all()])
    output = '<p><a href="/update">update</a></p>' + output
    return HttpResponse(output)

URL = "https://www.cbr.ru/scripts/XML_daily.asp"

def update(request):
    r = requests.get(URL)
    if r.status_code != 200: 
        raise Exception("cbr.ru bad response")
    rates = BeautifulSoup(r.content)
    with transaction.atomic():
        Rate.objects.all().delete()
        for rate in rates.valcurs.findAll("valute"):
            currency = rate.charcode.text
            rate = float(rate.value.text.replace(",", "."))
            Rate.objects.create(currency=currency, rate=rate)
    return redirect("/")
