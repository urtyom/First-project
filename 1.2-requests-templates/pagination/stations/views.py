import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page')

    csv_path = settings.BUS_STATION_CSV

    with open(csv_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        paginator = Paginator(list(reader), per_page=10)

        page_obj = paginator.get_page(page_number)

        context = {
            'bus_stations': page_obj.object_list,  # Список станций на текущей странице
            'page': page_obj,  # Текущая страница
        }

    return render(request, 'stations/index.html', context)
