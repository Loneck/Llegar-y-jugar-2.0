# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, ServicesForm, PaymentForm
from llegaryjugar.apps.reservations.views import StepWizard
from rest_framework.routers import DefaultRouter
from llegaryjugar.apps.reservations.viewsets import ScheduleViewSet


router = DefaultRouter()
router.register(r'schedule', ScheduleViewSet, 'schedule')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^$', StepWizard.as_view([ClubForm, ScheduleForm, ServicesForm, PaymentForm]), name='reservation'),
]
