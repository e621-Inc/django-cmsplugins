
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TextPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.text'
    verbose_name = _('Text Plugin')
