from django.db import models

from django.utils.translation import ugettext as _
from ajaximage.fields import AjaxImageField
from phonenumber_field.modelfields import PhoneNumberField

class Clubs(models.Model):
    name = models.CharField(_('name'), max_length=50)
    address = models.CharField(_('address'), max_length=50)
    description = models.TextField(_('description'))
    phone_number = PhoneNumberField()
    mail = models.EmailField()
    logo = AjaxImageField(_('image'), upload_to='clubs/logo/')
    latitude = models.DecimalField(_('latitude'), decimal_places=6, max_digits=20)
    length = models.DecimalField(_('length'), decimal_places=6, max_digits=20)
