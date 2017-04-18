from django.db import models

from django.utils.translation import ugettext as _


class PaymentMethods(models.Model):
	name = models.CharField(_('name'), max_length=50)
	status = models.CharField(_('status'), max_length=50)