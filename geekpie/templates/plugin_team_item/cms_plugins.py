from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import TeamItemModel

class TeamItemPlugin(CMSPluginBase):
    model = TeamItemModel
    name = _("Team Item Plugin")
    render_template = "plugins/TeamItemPlugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(TeamItemPlugin)
