from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Schedules
from .forms import SchedulesForm
# Create your views here.

class SchedulesList(ListView):
    model = Schedules

class SchedulesCreate(CreateView):
    model = Schedules
    fields = ['court', 'price', 'date', 'start_time', 'end_time']