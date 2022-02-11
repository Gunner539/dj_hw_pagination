from builtins import ValueError

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

import pagination.settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    try:
        page_number = int(request.GET.get('page', 1))
    except ValueError as v_er:
        page_number = 1

    page_content = get_stations_list()
    paginator = Paginator(page_content, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)

def get_stations_list():
    with open(pagination.settings.BUS_STATION_CSV, newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        page_content = []
        for row in reader:
            page_content.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    return page_content


