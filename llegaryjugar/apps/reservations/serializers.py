# -*- coding: utf-8 -*-
from rest_framework import serializers
from llegaryjugar.apps.schedules.models import Schedule
# from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    court = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Schedule
        fields = (
            'id',
            'court',
            'price',
            'date',
            'start_time',
            'end_time',
        )


class ReservationIsDoneSerializer(ReservationSerializer):

    class Meta(ReservationSerializer.Meta):
        fields = ('id',)
