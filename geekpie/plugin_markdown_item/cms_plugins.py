from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import MarkdownModel

import markdown

class MarkdownPlugin(CMSPluginBase):
    model = MarkdownModel
    name = _("Markdown Plugin")
    render_template = "plugins/MarkdownPlugin.html"
    change_form_template = "plugins/MarkdownPluginAdmin.html"
    cache = True
    allow_children = True  # This enables the parent plugin to accept child plugins
    child_classes = ['TextPlugin']

    def render(self, context, instance, placeholder):
        instance.content_html = markdown.markdown(instance.content)

        context['instance'] = instance

        return context

plugin_pool.register_plugin(MarkdownPlugin)
