# -*- coding: utf-8 -*-
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .serializers import ReservationSerializer, ReservationIsDoneSerializer
from llegaryjugar.apps.schedules.models import Schedule
# from .models import Task


class ReservationViewSet(viewsets.ReadOnlyModelViewSet,):

    model = Schedule
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Schedule.objects.all()

    @detail_route(methods=['put'])
    def set_is_done(self, request, pk=None):
        task = self.get_object()
        serializer = ReservationIsDoneSerializer(data=request.data)
        if serializer.is_valid():
            is_done = task.is_done
            task.is_done = not is_done
            task.save()
            return Response({'message': 'is done modified'},
                            status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
