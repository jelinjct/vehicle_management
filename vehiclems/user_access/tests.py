
from django.urls import reverse

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Vehicle

class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'list.html'
    context_object_name = 'vehicles'
    login_url = '/login/'


