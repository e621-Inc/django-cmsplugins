
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PicturesPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.pictures'
    verbose_name = _('Columns Pictures')
