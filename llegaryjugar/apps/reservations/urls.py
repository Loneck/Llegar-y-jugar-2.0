# -*- coding: utf-8 -*-
from django.conf.urls import url
from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, PaymentForm
from llegaryjugar.apps.reservations.views import StepWizard


urlpatterns = [
    url(r'^$', StepWizard.as_view([ClubForm, ScheduleForm, PaymentForm])),
]
