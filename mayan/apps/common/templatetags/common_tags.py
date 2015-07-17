from __future__ import unicode_literals

from json import dumps

from django.conf import settings
from django.template import Context, Library
from django.template.loader import get_template

import mayan

from ..utils import return_attrib

register = Library()


@register.filter
def get_encoded_parameter(item, parameters_dict):
    result = {}
    for attrib_name, attrib in parameters_dict.items():
        result[attrib_name] = return_attrib(item, attrib)
    return dumps(result)


@register.filter
def make_non_breakable(value):
    return value.replace('-', '\u2011')


@register.filter
def object_property(value, arg):
    return return_attrib(value, arg)


@register.simple_tag
def project_name():
    return settings.PROJECT_TITLE


@register.simple_tag
def project_version():
    return mayan.__version__


@register.assignment_tag(takes_context=True)
def render_subtemplate(context, template_name, template_context):
    """
    Renders the specified template with the mixed parent and
    subtemplate contexts
    """

    new_context = Context(context)
    new_context.update(Context(template_context))
    return get_template(template_name).render(new_context)
