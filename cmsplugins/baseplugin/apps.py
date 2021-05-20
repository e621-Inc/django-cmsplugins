
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BasePluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.baseplugin'
    verbose_name = _('Base Plugin')
