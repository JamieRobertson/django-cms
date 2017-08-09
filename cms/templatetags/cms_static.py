# -*- coding: utf-8 -*-
from django import template
from django.contrib.staticfiles.templatetags.staticfiles import StaticFilesNode

from cms.utils.urlutils import static_with_version


register = template.Library()


@register.tag('static_with_version')
def do_static_with_version(parser, token):
    """
    Joins the given path with the STATIC_URL setting
    and appends the CMS version as a GET parameter.

    Usage::
        {% static_with_version path [as varname] %}
    Examples::
        {% static_with_version "myapp/css/base.css" %}
        {% static_with_version variable_with_path %}
        {% static_with_version "myapp/css/base.css" as admin_base_css %}
        {% static_with_version variable_with_path as varname %}
    """
    return StaticWithVersionNode.handle_token(parser, token)


class StaticWithVersionNode(StaticFilesNode):
    """
    Subclass StaticFilesNode not StaticNode
    to make use of staticfiles_storage in production.
    """

    def url(self, context):
        url = super(StaticWithVersionNode, self).url(context)
        return static_with_version(url)
