
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TeasersPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.teasers'
    verbose_name = _('Teasers Plugin')
