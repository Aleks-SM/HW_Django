from django.shortcuts import render
from django.http import HttpResponse

from main.models import Product

def index_page(request):
    return HttpResponse("Hello")

def products_list(request):
    products = Product.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {'products': products})
