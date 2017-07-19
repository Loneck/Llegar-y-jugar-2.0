from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel


class ReservationsStatus(BaseModel):
    STATUS_RESERVED, STATUS_CONFIRMED = range(2)

    STATUS_CHOICES = (
        (STATUS_RESERVED, _(u'Reservada')),
        (STATUS_CONFIRMED, _(u'Confirmada'))
    )

    status = models.PositiveIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_RESERVED)

    def __str__(self):
        return '%s' % (self.get_status_display())
