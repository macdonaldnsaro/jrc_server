from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from dossier import settings

from typing import Any
from .models import *

def index(request: Any) -> HttpResponse:
    # if not request.session.has_key('currency'):
    #     request.session['currency'] = settings.DEFAULT_CURRENCY


    return render(
        request,
        template_name='profile.html',
        context={}
    )
