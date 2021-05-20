
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SlidersPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.sliders'
    verbose_name = _('Sliders Plugin')
