from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from django.utils import timezone
from django.db import models
from llegaryjugar.apps.schedules.models import Schedules 
from llegaryjugar.apps.courts.models import Courts 
from llegaryjugar.apps.payment_methods.models import PaymentMethods 
from llegaryjugar.apps.services.models import Services 
from llegaryjugar.apps.reservations_status.models import ReservationsStatus

class Courts(BaseModel):
	schedule = models.ForeignKey(Schedules, related_name='schedules', verbose_name=_('schedules'))
	court = models.ForeignKey(Courts, related_name='courts', verbose_name=_('courts'))
	client = models.ForeignKey('auth.User')
	payment = models.ForeignKey(PaymentMethods, related_name='payment', verbose_name=_('payment'))
	service = models.ForeignKey(Services, related_name='service', verbose_name=_('service'))
	status = models.ForeignKey(ReservationsStatus, related_name='reservations_status', verbose_name=_('reservations_status'))
	createdDate = models.DateTimeField(default=timezone.now)
