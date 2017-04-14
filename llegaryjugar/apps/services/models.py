from django.db import models

from django.utils.translation import ugettext as _


class Services(models.Model):
	name = models.CharField(_('name'), max_length=50)
	price = models.DecimalField(_('price'), decimal_places=2, max_digits=10)