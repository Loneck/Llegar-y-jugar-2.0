from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel

class CourtStatus(BaseModel):
	name = models.CharField(_('name'), max_length=50)