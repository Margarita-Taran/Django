from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phone = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phone = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone = Phone.objects.all().order_by('-price')
    else:
        phone = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
