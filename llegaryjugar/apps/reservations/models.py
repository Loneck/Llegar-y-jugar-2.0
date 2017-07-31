from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from django.utils import timezone
from llegaryjugar.apps.schedules.models import Schedule
from llegaryjugar.apps.courts.models import Courts
from llegaryjugar.apps.payment_methods.models import PaymentMethods
from llegaryjugar.apps.services.models import Services
from llegaryjugar.apps.reservations_status.models import ReservationsStatus
from llegaryjugar.apps.clubs.models import Clubs


class Reservation(BaseModel):
    schedule = models.ForeignKey(Schedule, related_name='res_schedule', verbose_name=_('schedule'))
    club = models.ForeignKey(Clubs, related_name='club_name', null=True)
    court = models.ForeignKey(Courts, related_name='res_courts', verbose_name=_('courts'))
    client = models.ForeignKey('auth.User')
    payment = models.ForeignKey(PaymentMethods, related_name='res_payment', verbose_name=_('payment'))
    service = models.ForeignKey(Services, related_name='res_service', verbose_name=_('service'))
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=30, null=True)
    status = models.ForeignKey(ReservationsStatus, related_name='res_reservationsStatus', verbose_name=_('reservationsStatus'))
    createdDate = models.DateTimeField(default=timezone.now)
