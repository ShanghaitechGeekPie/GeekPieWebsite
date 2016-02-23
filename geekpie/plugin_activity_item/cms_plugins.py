from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import ActivityItemModel

class ActivityItemPlugin(CMSPluginBase):
    model = ActivityItemModel
    name = _("Activity Item Plugin")
    render_template = "plugins/ActivityItemPlugin.html"
    cache = True
    allow_children = True  # This enables the parent plugin to accept child plugins
    child_classes = ['TextPlugin']

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ActivityItemPlugin)
