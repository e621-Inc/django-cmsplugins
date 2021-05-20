
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class IFramesPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.iframes'
    verbose_name = _('IFrames Plugin')
