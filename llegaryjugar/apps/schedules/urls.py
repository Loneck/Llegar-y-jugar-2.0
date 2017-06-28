from django.conf.urls import include, url
from .views import SchedulesList, SchedulesCreate

urlpatterns = [
	url(r'^$', SchedulesList.as_view(), name='schedules-list'),
	url(r'schedules/add/$', SchedulesCreate, name='schedules-add'),
]