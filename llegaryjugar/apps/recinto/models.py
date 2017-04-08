from django.db import models

from django.utils.translation import ugettext as _
from ajaximage.fields import AjaxImageField

class Recinto(models.Model):
    id_recinto = models.AutoField(primary_key=True)
    nombre = models.CharField(_('nombre'), max_length=50)
    direccion = models.CharField(_('dirección'), max_length=50)
    descripcion = models.TextField(_('descripción'))
    telefono = models.DecimalField(_('telefono'), decimal_places=0, max_digits=9)
    correo = models.CharField(_('correo'), max_length=50)
    logo = AjaxImageField(_('image'), upload_to='clubs/logo/')
    latitud = models.DecimalField(_('latitud'), decimal_places=6, max_digits=20)
    longitud = models.DecimalField(_('longitud'), decimal_places=6, max_digits=20)
