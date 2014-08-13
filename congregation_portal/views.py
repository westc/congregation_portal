from django.core.context_processors import csrf
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import util


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
        return redirect(onsuccess)
    else:
        messages.error(request, util.msgs['msg_login'])
        return redirect(onfail)


@login_required(login_url='/login/')
def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def territory(request):
    context = {}
    return render(request, 'territory.html', context)
