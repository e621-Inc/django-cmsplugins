
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VideosPluginConfig(AppConfig):

    default_auto_field = 'django.db.models.AutoField'
    name = 'cmsplugins.videos'
    verbose_name = _('Videos Plugin')
