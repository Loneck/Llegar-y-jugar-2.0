from django.forms import ModelForm, inlineformset_factory

from .models import Schedules


class SchedulesForm(ModelForm):
	class Meta:
		model = Schedules
		exclude = ()
		