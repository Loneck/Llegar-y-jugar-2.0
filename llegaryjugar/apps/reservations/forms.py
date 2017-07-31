from django import forms
from llegaryjugar.apps.schedules.models import Schedule
from llegaryjugar.apps.reservations.models import Reservation


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
        fields = ('schedule',)


# class AccesorieForm(ClubForm):

#     def __init__(self, *args, **kwargs):
#         super(AccesorieForm, self).__init__(*args, **kwargs)
#         self.fields['accesorie'].queryset = Accesorie.objects.filter(club=self.club)

#     class Meta(ClubForm.Meta):
#         fields = ('accesorie',)


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.price = kwargs.pop('price', None)
        kwargs.update(initial={'price': self.price})
        super(PaymentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Reservation
        fields = ('price',)
