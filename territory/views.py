from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from congregation_portal import util

from territory import models as territory_models
from congregation_portal import models as shared_models


@login_required(login_url='/login/')
def territory(request):
    congregation = shared_models.Congregation.objects.get(pk=request.session.get('congregation'))
    territories = territory_models.Territory.objects.filter(congregation=congregation)
    context = {'territories': territories,
               'congregations': util.congregations}
    return render(request, 'territory.html', context)


def territory_reports(request):
    congregation = shared_models.Congregation.objects.get(pk=request.session.get('congregation'))
    territories = territory_models.Territory.objects.filter(congregation=congregation)
    context = {'territories': territories,
               'congregations': util.congregations}
    return render(request, 'territory_reports.html', context)