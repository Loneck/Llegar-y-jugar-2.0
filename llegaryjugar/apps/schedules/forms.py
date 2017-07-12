# -*- coding: utf-8 -*-
from django.forms import ModelForm, forms

from .models import Schedules, SchedulesCreate


class SchedulesForm(ModelForm):
	class Meta:
		model = Schedules
		fields = [
			'court',
			'price',
			'date',
			'start_time',
			'end_time',
		]

	def __init__(self, *args, **kwargs):
	    super(SchedulesForm, self).__init__(*args, **kwargs)
	    self.fields['court'].widget.attrs['class'] = 'form-control'
	    self.fields['price'].widget.attrs['class'] = 'form-control'
	    self.fields['date'].widget.attrs['class'] = 'form-control'
	    self.fields['start_time'].widget.attrs['class'] = 'form-control'
	    self.fields['end_time'].widget.attrs['class'] = 'form-control'

class MultipleSchedulesForm(ModelForm):
	class Meta:
		model = SchedulesCreate
		fields = [
			'price',
			'day',
			'month',
			'start_time',
			'end_time',
		]

	def __init__(self, *args, **kwargs):
	    super(MultipleSchedulesForm, self).__init__(*args, **kwargs)
	    self.fields['price'].widget.attrs['class'] = 'form-control'
	    self.fields['day'].widget.attrs['class'] = 'form-control'
	    self.fields['month'].widget.attrs['class'] = 'form-control'
	    self.fields['start_time'].widget.attrs['class'] = 'form-control'
	    self.fields['end_time'].widget.attrs['class'] = 'form-control'