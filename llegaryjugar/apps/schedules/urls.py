# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from .views import ScheduleList, SchedulesCreate, MultipleSchedulesCreate

urlpatterns = [
	url(r'^$', ScheduleList.as_view(), name='schedules-list'),
	url(r'^add/$', SchedulesCreate, name='schedules-add'),
	url(r'^multiple-add/$', MultipleSchedulesCreate, name='schedules-multiple-add'),
]