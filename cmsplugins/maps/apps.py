
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MapsPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.maps'
    verbose_name = _('Maps Plugin')
