# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.http import HttpResponse

from .models import Schedules, SchedulesCreate
from .forms import SchedulesForm, MultipleSchedulesForm
# Create your views here.

class SchedulesList(ListView):
	model = Schedules

def SchedulesCreate(request):
	if request.method == 'POST':
		form = SchedulesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('schedules-list')
	else:
		form = SchedulesForm()
	return render(request, 'schedules/schedules_form.html', {'form':form})

def MultipleSchedulesCreate(request):
	if request.method == 'POST':
		form = MultipleSchedulesForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('schedules-list')
	else:
		form = MultipleSchedulesForm()
	return render(request, 'schedules/schedules_multiple-form.html', {'form':form})
