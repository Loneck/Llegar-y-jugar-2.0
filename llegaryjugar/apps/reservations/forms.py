from django import forms
from llegaryjugar.apps.schedules.models import Schedule
from llegaryjugar.apps.reservations.models import Reservation
from llegaryjugar.apps.services.models import Service


class ClubForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.club = kwargs.pop('club', None)
        super(ClubForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Reservation
        fields = ('club',)


class ScheduleForm(ClubForm):

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['schedule'].queryset = Schedule.objects.filter(court__club=self.club)

    class Meta(ClubForm.Meta):
        fields = ('schedule', 'court')


class ServicesForm(ClubForm):

    def __init__(self, *args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(club=self.club)

    class Meta(ClubForm.Meta):
        fields = ('service',)


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.price = kwargs.pop('price', None)
        kwargs.update(initial={'price': self.price})
        super(PaymentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Reservation
        fields = ('price',)
