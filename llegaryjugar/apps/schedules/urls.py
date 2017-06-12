from django.conf.urls import include, url
from .import views

urlpatterns = [
	url(r'^$', views.SchedulesList.as_view(), name='schedules-list'),
	url(r'schedules/add/$', views.SchedulesCreate.as_view(), name='schedules-add'),
]