from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView
from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, PaymentForm
from llegaryjugar.apps.reservations.models import Reservation


# Create your views here.
class StepWizard(SessionWizardView):
    template_name = 'wizard_form.html'
    form_list = [ClubForm, ScheduleForm, PaymentForm]
    instance = None
    price = None

    def get_form_kwargs(self, step=None):
        kwargs = {}
        if step == '1' or step == '2':
            club = self.get_cleaned_data_for_step('0')['club']
            kwargs.update({'club': club})
        if step == '3':
            schedule = self.get_cleaned_data_for_step('1')['schedule']
            self.price = schedule.price
            kwargs.update({'price': self.price})
        return kwargs

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Reservation()
        return self.instance

    def done(self, form_list, **kwargs):

        data = {}
        for form in form_list:
            data.update(form.cleaned_data)
        reservation = Reservation.objects.create(**data)
        reservation.author = self.request.user
        reservation.save()
        return render_to_response('done.html', {'reservation': reservation})
