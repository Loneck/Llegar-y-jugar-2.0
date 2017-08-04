from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel


class PaymentMethod(BaseModel):
    name = models.CharField(_('name'), max_length=50)
    status = models.CharField(_('status'), max_length=50)

    def __unicode__(self):
        return '%s' % (self.name)
