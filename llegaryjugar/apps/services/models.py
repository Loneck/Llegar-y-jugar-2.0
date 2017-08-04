from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club


class Service(BaseModel):
    club = models.ForeignKey(Club, related_name='club_accesorie', verbose_name=_('club'), null=True)
    name = models.CharField(_('name'), max_length=50)
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=10)
    is_active = models.BooleanField(_('is active'), default=True)

    def __unicode__(self):
        return '%s' % (self.name)
