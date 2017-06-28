from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.http import HttpResponse

from .models import Schedules
from .forms import SchedulesForm
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

