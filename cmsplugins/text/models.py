from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.models import BasePlugin


class Text(BasePlugin):
    """
    Plain Text Plugin
    """

    body = models.TextField(
        default='',
        verbose_name=_('body'),
    )

    def __str__(self):
        string = strip_tags(' '.join(self.body.splitlines()))
        return '{0}'.format(string[:60])
