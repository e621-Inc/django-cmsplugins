
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HeadersPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.headers'
    verbose_name = _('Headers Plugin')
