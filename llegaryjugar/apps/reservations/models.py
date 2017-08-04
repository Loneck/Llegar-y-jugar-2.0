from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from django.utils import timezone
from llegaryjugar.apps.schedules.models import Schedule
from llegaryjugar.apps.courts.models import Court
from llegaryjugar.apps.payment_methods.models import PaymentMethod
from llegaryjugar.apps.services.models import Service
from llegaryjugar.apps.reservations_status.models import ReservationsStat
from llegaryjugar.apps.clubs.models import Club


class Reservation(BaseModel):
    schedule = models.ForeignKey(Schedule, related_name='res_schedule', verbose_name=_('schedule'))
    club = models.ForeignKey(Club, related_name='club_name', null=True)
    court = models.ForeignKey(Court, related_name='res_courts', verbose_name=_('courts'))
    client = models.ForeignKey('auth.User', null=True, default=True)
    payment = models.ForeignKey(PaymentMethod, related_name='res_payment', verbose_name=_('payment'), default=1)
    service = models.ForeignKey(Service, related_name='res_service', verbose_name=_('service'))
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=30, null=True)
    status = models.ForeignKey(ReservationsStat, related_name='res_reservationsStatus', verbose_name=_('reservationsStatus'), default=1)
    createdDate = models.DateTimeField(default=timezone.now)
