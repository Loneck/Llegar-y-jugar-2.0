# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .serializers import ScheduleSerializer
from llegaryjugar.apps.schedules.models import Schedule
from django_filters.rest_framework import DjangoFilterBackend
# from .models import Task


class ScheduleViewSet(viewsets.ReadOnlyModelViewSet,):

    model = Schedule
    serializer_class = ScheduleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('court', 'date')

    def get_queryset(self):
        return Schedule.objects.all()
