from django.db import models

from django.utils.translation import ugettext as _


class CourtStatus(models.Model):
	name = models.CharField(_('name'), max_length=50)
