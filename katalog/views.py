from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_item': data_barang_katalog,
    'nama': 'Adish',
    'studentID': '2106751285'
    }
    return render(request, "katalog.html", context)