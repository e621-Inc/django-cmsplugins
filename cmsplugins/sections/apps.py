
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SectionsPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.sections'
    verbose_name = _('Sections Plugin')
