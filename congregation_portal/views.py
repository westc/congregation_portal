from django.core.context_processors import csrf
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import util

from territory import models as territory_models
from congregation_portal import models as shared_models


def login_view(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is not None:
        login(request, user)
        request.session['congregation'] = user.profile.congregation.number
        return redirect(onsuccess)
    else:
        messages.error(request, util.msgs['msg_login'])
        return redirect(onfail)


@login_required(login_url='/login/')
def index(request):
    context = {'congregations': util.congregations}
    return render(request, 'index.html', context)


@login_required(login_url='/login/')
def territory(request):
    congregation = shared_models.Congregation.objects.get(pk=request.session.get('congregation'))
    territories = territory_models.Territory.objects.filter(congregation=congregation)
    context = {'territories': territories,
               'congregations': util.congregations}
    return render(request, 'territory.html', context)


@login_required(login_url='/login/')
def change_congregation(request):
    if request.user.profile.admin:
        request.session['congregation'] = request.POST['congregation']
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, util.msgs['msg_insufficient_privileges'])
        return redirect(request.META.get('HTTP_REFERER'))
