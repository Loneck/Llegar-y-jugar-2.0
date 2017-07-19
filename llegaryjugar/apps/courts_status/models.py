from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel


class CourtStatus(BaseModel):
    STATUS_AVAILABLE, STATUS_NOT_AVAILABLE, STATUS_RESERVED, STATUS_CONFIRMED = range(4)

    STATUS_CHOICES = (
        (STATUS_NOT_AVAILABLE, _(u'No Disponible')),
        (STATUS_AVAILABLE, _(u'Disponible')),
        (STATUS_RESERVED, _(u'Reservada')),
        (STATUS_CONFIRMED, _(u'Confirmada'))
    )

    status = models.PositiveIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_AVAILABLE)

    def __str__(self):
        return '%s' % (self.get_status_display())
