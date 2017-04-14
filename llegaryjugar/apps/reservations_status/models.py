from django.db import models

from django.utils.translation import ugettext as _


class Reservations_status(models.Model):
	name = models.CharField(_('name'), max_length=50)