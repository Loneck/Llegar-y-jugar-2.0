# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from .views import SchedulesList, SchedulesCreate, MultipleSchedulesCreate

urlpatterns = [
	url(r'^$', SchedulesList.as_view(), name='schedules-list'),
	url(r'^add/$', SchedulesCreate, name='schedules-add'),
	url(r'^multiple-add/$', MultipleSchedulesCreate, name='schedules-multiple-add'),
]