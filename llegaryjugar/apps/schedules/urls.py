# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import Schedule_List, Schedules_Create, Multiple_Schedules_Create

urlpatterns = [
    url(r'^$', Schedule_List.as_view(), name='schedules-list'),
    url(r'^add/$', Schedules_Create, name='schedules-add'),
    url(r'^multiple-add/$', Multiple_Schedules_Create, name='schedules-multiple-add'),
]
