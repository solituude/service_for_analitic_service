from django.shortcuts import render

from .forms import FindForm
from .models import Ads


def home_view(request):

    form = FindForm()
    city = request.GET.get('city')
    count_rooms = request.GET.get('count_rooms')
    material = request.GET.get('material')
    conditions = request.GET.get('conditions')
    segment = request.GET.get('segment')
    have_balcony = request.GET.get('have_balcony')

    qs = []

    if city or material or conditions or segment or have_balcony or count_rooms:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if count_rooms:
            _filter['count_rooms__slug'] = count_rooms
        if material:
            _filter['material__slug'] = material
        if conditions:
            _filter['conditions__slug'] = conditions
        if segment:
            _filter['segment__slug'] = segment
        if have_balcony:
            _filter['have_balcony__slug'] = have_balcony
        if count_rooms:
            _filter['count_rooms__slug'] = count_rooms

        qs = Ads.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs, 'form': form})

