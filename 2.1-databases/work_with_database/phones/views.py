from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'min_price':
        sort = 'price'
    elif sort == 'max_price':
        sort = '-price'
    elif sort == 'name':
        sort = 'name'
    phones = Phone.objects.order_by(sort).all()
    template = 'catalog.html'
    print(phones)
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug = slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
