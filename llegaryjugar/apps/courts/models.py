from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.courts_status.models import CourtStat


class Court(BaseModel):
    club = models.ForeignKey(
        Club,
        related_name='club',
        verbose_name=_('club'),
    )
    status = models.ForeignKey(
        CourtStat,
        related_name='court_status',
        verbose_name=_('status'),
    )
    name = models.CharField(
        _('name'),
        max_length=50,
    )
    number = models.CharField(
        _('number'),
        max_length=50,
    )

    def __unicode__(self):
        return self.name
