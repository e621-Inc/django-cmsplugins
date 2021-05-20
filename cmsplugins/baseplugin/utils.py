from importlib import import_module

from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _


def get_indicator_hidden(request, instance):
    html = ''
    is_visible = getattr(instance, 'is_visible', True)
    if request.toolbar.edit_mode_active and not is_visible:
        name = _('hidden')
        css_class = 'plugin-indicator-hidden'
        html = '<span class="{}">{}</span>'.format(
            css_class,
            name,
        )
    return mark_safe(html)


def get_str_from_tuple(key='', properties=()):
    return dict((k, v) for k, v in properties).get(key, '')


def get_model(import_path):

    module_name, object_name = import_path.rsplit('.', 1)
    module = import_module(module_name)
    return getattr(module, object_name)
