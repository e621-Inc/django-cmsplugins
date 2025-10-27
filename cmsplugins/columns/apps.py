
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ColumnsPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.columns'
    verbose_name = _('Columns Plugin')
