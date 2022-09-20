from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
    'list_watch': data_watchlist,
    'nama': 'Adish',
    'studentID': '2106751285'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
    'list_watch': data_watchlist,
    'nama': 'Adish',
    'studentID': '2106751285'
    }
    return render(request, "mywatchlist.html", context)