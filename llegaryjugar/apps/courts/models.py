from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.clubs.models import Clubs 
from llegaryjugar.apps.courts_status.models import Court_status

class Courts(models.Model):
	club = models.ForeignKey(Clubs, related_name='club', verbose_name=_('club'))
	status = models.ForeignKey(Court_status, related_name='status', verbose_name=_('status'))
	name = models.CharField(_('name'), max_length=50)
	number = models.CharField(_('number'), max_length=50)
